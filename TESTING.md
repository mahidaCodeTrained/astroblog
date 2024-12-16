Return to the [README.md](README.md) file.

## Table of Contents

<details>
<summary>Click here for Table of Contents</summary>

- [Validation](#validation)

- [Lighthouse](#lighthouse)

- [User Story Testing](#user-story-testing)

- [Input Testing](#input-testing)

- [Manual Testing](#manual-testing)

- [User Validation Testing](#user-validation-testing)

- [Bugs](#bugs)

</details>

## Validation 
- This will show that the code is completely validated and correctly placed.

### HTML

| Page | URL | Screenshot | Notes |
| :---: | :---: | :---: | :---: |
| home | [W3C](https://validator.w3.org/) | ![screenshot](assets/readmefiles/validation/homevalidator.jpg) | Passed all checks |
| createpost | [W3C](https://validator.w3.org/) | ![screenshot](assets/readmefiles/validation/createpostvalidation.jpg) | Passed all checks |
| editpost | [W3C](https://validator.w3.org/) | ![screenshot](assets/readmefiles/validation/editvalidation.jpg) | Passed all checks |
| detailed posts | [W3C](https://validator.w3.org/) | ![screenshot](assets/readmefiles/validation/detailedpostvalidator.jpg) | Passed all checks |
| profile | [W3C](https://validator.w3.org/) | ![screenshot](assets/readmefiles/validation/profilevalidation.jpg) | Passed all checks |
| sign in | [W3C](https://validator.w3.org/) | ![screenshot](assets/readmefiles/validation/signinvalidation.jpg) | Passed all checks |
| sign out | [W3C](https://validator.w3.org/) | ![screenshot](assets/readmefiles/validation/signoutvalidation.jpg) | Passed all checks |

- The about page uses crispyform styling from the django admin to create the page and it makes its own tags like font which wasnt compatible with W3C. The site works perfectly and it looks perfect.

### CSS

| Page | Jigsaw URL | Screenshot | Notes |
| :---: | :---: | :---: | :---: |
| style.css | [Jigsaw](https://jigsaw.w3.org/css-validator/validator) | ![screenshot](assets/readmefiles/validation/cssvalidator.jpg) | Passed all checks |


### JavaScript

| Page | JS Hint URL | Screenshot | Notes |
| :---: | :---: | :---: | :---: |
| script.js | [JS Hint](https://jshint.com/) | ![screenshot](documentation/testing/javascriptvalidator.png) | This has passed all checks, the two unused functions that can be seen stated are not an error in the JS code. It is simply because those functions are not being called upon at the current moment. |



### Python

| File | URL | Screenshot | Notes |
| :---: | :---: | :---: | :---: |
|  | [CI Python Linter](https://pep8ci.herokuapp.com/#) | ![screenshot](documentation/testing/pythonlinter-success.png) | Passed all checks |

## Lighthouse
- This is the lighthouse testing section for all of the pages. 

| Page   | Mobile                                                                                  | Desktop                                                                                   | Notes                                                                                                                                                                         |
| :----: | :-------------------------------------------------------------------------------------: | :---------------------------------------------------------------------------------------: | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| base.html/index.html | ![screenshot](assets/readmefiles/lighthouse/homelighthousedesktop.jpg) | ![screenshot](assets/readmefiles/lighthouse/homelighthouse.jpg) | The low scores in best practices are because of Cloudinary and users posting their images for the blogs. |
| detailed_posts.html | ![screenshot](assets/readmefiles/lighthouse/detailedpostlighthousedesktop.jpg) | ![screenshot](assets/readmefiles/lighthouse/detailedpostlighthousedesk.jpg) | The scores are overall very high. |
| about | ![screenshot](assets/readmefiles/lighthouse/aboutlighthousedesktop.jpg) | ![screenshot](assets/readmefiles/lighthouse/aboutmobilelighthouse.jpg) | The performance is low due to the high render images however the rest is very good practice and SEO |
| create post | ![screenshot](assets/readmefiles/lighthouse/createpostdesktoplighthouse.jpg) | ![screenshot](assets/readmefiles/lighthouse/createpostmobilelight.jpg) | High Performance in the sight!. |
| edit post | ![screenshot](assets/readmefiles/lighthouse/editpostlighthouseactualdesktop.jpg) | ![screenshot](assets/readmefiles/lighthouse/editmobile.jpg) | High Performance in the sight!. |
| profile | ![screenshot](assets/readmefiles/lighthouse/profilelighthousedesktop.jpg) | ![screenshot](assets/readmefiles/lighthouse/profilemob.jpg) | The low scores are due to users being able to upload their own images thats the reason for the performance and best practices being low. Cloudinary causes bad performance due to the level of images. |
| sign out | ![screenshot](assets/readmefiles/lighthouse/signoutlighthousedesktop.jpg) | ![screenshot](assets/readmefiles/lighthouse/usersignoutmobile.jpg) | Very high performance and SEO! |
| sign in | ![screenshot](assets/readmefiles/lighthouse/signinlighthousedesktop.jpg) | ![screenshot](assets/readmefiles/lighthouse/signinmobilelighthouse.jpg) | page works very well |
| sign up | ![screenshot](assets/readmefiles/lighthouse/signupdesktoplh.jpg) | ![screenshot](assets/readmefiles/lighthouse/signupmobilelh.jpg) | near perfect |

- The pages work very well considering how many images are being passed in the blog. Cloudinary does cause alot of these performance and best practice issues it is important to remember that.