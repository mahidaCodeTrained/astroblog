/*JavaScript code taken from Code Institute I think therefore I blog*/ 

const editButtons = document.getElementsByClassName("btn-edit");
const commentText = document.getElementById("id_body");
const commentForm = document.getElementById("commentForm");
const submitButton = document.getElementById("submitButton");
const commentSection = document.getElementById("comment-section"); // Ensure this ID matches your "Leave a comment" section.

// Modal related to delete
const deleteModal = (document.getElementById("deleteModal"));
const deleteButtons = document.getElementsByClassName("btn-delete");
const deleteConfirm = document.getElementById("deleteConfirm");
const closeModalButton = document.querySelector("#deleteModal .btn-close"); // Selecting the close button inside the modal

// Scroll to the comment form section
for (let button of editButtons) {
  button.addEventListener("click", (e) => {
    let commentId = e.target.getAttribute("comment_id");
    let commentContent = document.getElementById(`comment${commentId}`).innerText;
    commentText.value = commentContent;
    submitButton.innerText = "Update";
    commentForm.setAttribute("action", `edit_comment/${commentId}`);

    // Scroll to the Leave a comment section smoothly
    commentSection.scrollIntoView({ behavior: 'smooth' });
  });
}

// Open delete modal when delete button is clicked
for (let button of deleteButtons) {
    button.addEventListener("click", (e) => {
      let commentId = e.target.getAttribute("comment_id");
      deleteConfirm.href = `delete_comment/${commentId}`;
      deleteModal.show();
    });
}

// Close the modal when the close button is clicked
if (closeModalButton) {
  closeModalButton.addEventListener("click", () => {
    deleteModal.hide();
  });
}
