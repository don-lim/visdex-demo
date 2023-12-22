// JavaScript to handle the file upload and display the image
document.addEventListener("DOMContentLoaded", function () {
    const fileInput = document.querySelector("#file-input");
    const searchButton = document.querySelector(".search-button");
    const uploadResults = document.querySelector("#upload-results");
    const uploadResultsTitle = document.querySelector("#upload-results-title");
    const searchResults = document.querySelector("#search-results");
    const loadingElement = document.querySelector("#loading");

    // Get the drop zone element
    const dropzone = document.querySelector("#dropzone");

    // Add event listeners for drag and drop events
    dropzone.addEventListener("dragover", function (event) {
        event.preventDefault();
        dropzone.classList.add("dragging");
    });

    dropzone.addEventListener("dragleave", function () {
        dropzone.classList.remove("dragging");
    });

    dropzone.addEventListener("drop", function (event) {
        event.preventDefault();
        dropzone.classList.remove("dragging");

        // Get the dropped files
        const files = event.dataTransfer.files;

        // If a file was dropped, trigger the file input's change event
        if (files.length) {
            fileInput.files = files;
            fileInput.dispatchEvent(new Event("change"));
        }
    });

    dropzone.addEventListener("click", function () {
        fileInput.click();
    });

    // Function to display search results
/*    function displaySearchResults(results) {
        // display the search results here
        searchResults.innerHTML = "<p>Search results will be displayed here.</p>";
    } */

// Function to display search results
function displaySearchResults(results, image_base64) {
    // Check if results and image_base64 are arrays and not undefined
    if (Array.isArray(results) && Array.isArray(image_base64) && results.length > 0) {
        // Get the search results container
        const searchResultsContainer = document.querySelector("#search-results");

        // Clear previous search results
        searchResultsContainer.innerHTML = "";

        // Iterate through the search results and create elements for each result
        results.forEach((result, index) => {
            // Create a container div for each result
            const resultContainer = document.createElement("div");
            resultContainer.classList.add("result-container");

            // Create a div for centering
            const centerDiv = document.createElement("div");
            centerDiv.classList.add("centered-content");

            // Create a site paragraph
            const productSite = document.createElement("p");
            productSite.classList.add("site-info");
            productSite.textContent = "" + result.site; // Set the site text

            // Create a title element for the product
            const productTitle = document.createElement("h3");
            productTitle.textContent = result.productDisplayName; // Set the product title

            // Create an image element for the product with a link
            const productLink = document.createElement("a");
            productLink.href = result.referralLink; // Set the href attribute
            productLink.target = "_blank"; // Open link in a new tab

            const productImage = document.createElement("img");
            if (image_base64[index]) {
                productImage.src = "data:image/jpeg;base64," + image_base64[index]; // Set the base64 image source
            }
            productImage.alt = result.productDisplayName; // Set the alt text
            productImage.classList.add("product-image"); // Add a CSS class
            productImage.style.width = "200px"; // Set the image width to 200px

            // Create a price paragraph
            const productPrices = document.createElement("p");
            productPrices.classList.add("price-info");
            productPrices.textContent = "" + result.prices; // Set the prices text

            // Append the site, title, image with link, and price
            centerDiv.appendChild(productSite);
            centerDiv.appendChild(productTitle);
            productLink.appendChild(productImage); // Link wraps the image
            centerDiv.appendChild(productLink);
            centerDiv.appendChild(productPrices);

            // Append the centering div to the result container
            resultContainer.appendChild(centerDiv);

            // Append the result container to the search results container
            searchResultsContainer.appendChild(resultContainer);
        });
        loadingElement.style.display = "none";
    } else {
        // Handle the case where no results were found
        searchResults.innerHTML = "<p>No results found.</p>";
        loadingElement.style.display = "none";
    }
}



    // Add an event listener to the SEARCH PRODUCT button
    searchButton.addEventListener("click", function (event) {
        event.preventDefault(); // Prevent the form from submitting

        // Check if an image is uploaded
        if (!fileInput.files[0]) {
            alert("Please choose an image to search.");
            return;
        }

        loadingElement.style.display = "block";

        // Send a POST request to the server to initiate the search
        const formData = new FormData();
        formData.append("image", fileInput.files[0]);

        fetch("/search", {
            method: "POST",
            body: formData,
        })
            .then((response) => response.json())
            .then((data) => {
                if (data.success) {
                    // Handle the search results
                    displaySearchResults(data.results, data.image_base64);
                } else {
                    console.error(data.message);
                }
            })
            .catch((error) => {
                console.error("Error:", error);
            });
    });

    // Add an event listener to the CHOOSE FILE button
    fileInput.addEventListener("change", function () {
        const file = fileInput.files[0];
        if (file) {
            // Clear previous content
            uploadResults.innerHTML = "";
            uploadResultsTitle.style.display = "";

            // Reset search results
            searchResults.innerHTML = "";

            const reader = new FileReader();

            reader.onload = function (event) {
                // Create a new <div> container for the image and apply centering CSS
                const containerDiv = document.createElement("div");
                containerDiv.style.textAlign = "center"; // Center align the contents

                // Create a new <img> element with the data URL as the source
                const uploadedImage = document.createElement("img");
                uploadedImage.src = event.target.result; // Data URL
                uploadedImage.alt = "Uploaded Image";

                // Set the image width to 200 pixels
                uploadedImage.width = 200;

                // Append the <img> element to the container <div>
                containerDiv.appendChild(uploadedImage);

                // Append the container <div> to the upload results section
                uploadResults.appendChild(containerDiv);

                // Send a POST request to the server to upload the file
                const formData = new FormData();
                formData.append("image", file);

                fetch("/upload", {
                    method: "POST",
                    body: formData,
                })
                    .then((response) => response.json())
                    .then((data) => {
                        if (data.success) {
                            // Handle any server response data as needed
                        } else {
                            console.error(data.message);
                        }
                    })
                    .catch((error) => {
                        console.error("Error:", error);
                    });
            };

            // Read the file as a data URL
            reader.readAsDataURL(file);
        }
    });
});
