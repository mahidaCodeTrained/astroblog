document.addEventListener("DOMContentLoaded", function () {
    // Listen for all pagination link clicks
    const paginationLinks = document.querySelectorAll('.pagination a');

    paginationLinks.forEach(link => {
        link.addEventListener('click', function (e) {
            e.preventDefault(); // Prevent default page refresh on pagination clicks

            const targetPage = link.getAttribute('href'); // Get the href from the clicked link
            const contentDiv = document.getElementById('content'); // Div where posts will be loaded

            // Save the current scroll position before loading new content
            const currentScrollPosition = window.scrollY;

            // Use the Fetch API to get the content for the target page
            fetch(targetPage)
                .then(response => response.text())
                .then(html => {
                    // Extract the new content from the fetched HTML
                    const newContent = html.match(/<div class="container".*<\/div>/s)[0];
                    contentDiv.innerHTML = newContent;  // Replace the content

                    // Update the browser URL without reloading the page
                    window.history.pushState(null, '', targetPage);

                    // Restore the scroll position to where it was before the new content loaded
                    window.scrollTo(0, currentScrollPosition);
                })
                .catch(error => console.error('Error fetching new content:', error));
        });
    });
});
