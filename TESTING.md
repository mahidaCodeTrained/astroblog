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