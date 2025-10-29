Protein Bite testing screenshots

## HTML
I have used the recommended [HTML W3C Validator](https://validator.w3.org/) to validate all of my HTML files.

| Page | Screenshot | Notes |
| ---- | ---------- | ----- | 
| Home | ![htmlhome](TESTING-screenshots/html-validatorcheck-homepage.png) | Pass - No Errors |
| About | ![htmlabout](TESTING-screenshots/html-validatorcheck-aboutpage.png) | Pass - No Errors |
| Account | ![htmlaccount](TESTING-screenshots/html-validatorcheck-accountpage.png) | HTTP resource not retrievable Error |
| login | ![htmllogin](TESTING-screenshots/html-validatorcheck-loginpage-error.png) | Style coding was in the wrong area Error |
| login | ![htmllogin](TESTING-screenshots/html-validatorcheck-loginpage-pass.png) | Fixed error- Pass - No Errors |
| Recipe | ![htmlrecipe](TESTING-screenshots/html-validatorcheck-recipepage.png) | Pass - No Errors |
| Recipe 1 | ![htmlrecipe1](TESTING-screenshots/html-validatorcheck-recipepage1.png) | Pass - No Errors |
| Recipe 2 | ![htmlrecipe2](TESTING-screenshots/html-validatorcheck-recipepage2.png) | Pass - No Errors |
| Recipe 3 | ![htmlrecipe3](TESTING-screenshots/html-validatorcheck-recipepage3.png) | Pass - No Errors |
| Recipe 4 | ![htmlrecipe4](TESTING-screenshots/html-validatorcheck-recipepage4.png) | Pass - No Errors |
| Recipe 5 | ![htmlrecipe5](TESTING-screenshots/html-validatorcheck-recipepage5.png) | Pass - No Errors |
| Recipe 6 | ![htmlrecipe6](TESTING-screenshots/html-validatorcheck-recipepage6.png) | Pass - No Errors |
| Recipe 7 | ![htmlrecipe7](TESTING-screenshots/html-validatorcheck-recipepage7.png) | Pass - No Errors |

## CSS
I have used the recommended [CSS Jigsaw Validator](https://jigsaw.w3.org/css-validator/) to validate all of my CSS files.

| File | Screenshot | Notes |
| ---- | ---------- | ----- |
| CSS Screenshot | ![css](TESTING-screenshots/cssvalidationscreenshot.png) | This error is from the enivorment I installed, I have tried to search for it but can't find the line of code. The warnings are also extensions |

## Python
I have used the [PEP8 CI Python Linter](https://pep8ci.herokuapp.com/) to validate my Python files.

| Page | Screenshot | Notes |
| ---- | ---------- | ----- |
| admin | ![pythonadmin](TESTING-screenshots/pythonadmin.png) | one line too long |
| apps | ![pythonapps](TESTING-screenshots/pythonapps.png) | pass - No Errors |
| asgi | ![pythonasgi](TESTING-screenshots/pythonasgi.png) | pass - No Errors |
| forms | ![pythonforms](TESTING-screenshots/pythonforms.png) | pass - No Errors |
| init | ![pythoninit](TESTING-screenshots/pythoninit.png) | pass - No Errors |
| manage | ![pythonmanage](TESTING-screenshots/pythonmanage.png) | pass - No Errors |
| models | ![pythonmodels](TESTING-screenshots/pythonmanage.png) | pass - No Errors |
| settings | ![pythonsettings](TESTING-screenshots/pythonsettings.png) | lines too long |
| urls | ![pythonurls](TESTING-screenshots/pythonurls.png) | lines too long |
| views | ![pythonviews](TESTING-screenshots/pythonviews.png) | expected 2 blank lines, no space in the comment, whitespace, code in the wrong area |
| views | ![pythonviews-pass](TESTING-screenshots/pythonviews-pass.png) | fixed errors: pass - No Errors |

## Browser Compatability

| Page | Screenshot | Notes |
| ---- | ---------- | ----- |
| Chrome | ![chrome](TESTING-screenshots/chrome.png) | No problems |
| Firefox | ![firefox](TESTING-screenshots/firefox.png) | No problems |
| Microsoft Edge | ![edge](TESTING-screenshots/microsoftedge.png) | No problems |

## Lighthouse
I've tested my deployed project using the Lighthouse tool to check for issues.

| Page | Screenshot |
| ---- | ---------- |
| Home | ![lighthousehome](TESTING-screenshots/lighthouse-home.png) |
| About | ![lighthouseabout](TESTING-screenshots/lighthouse-about.png) |
| Account | ![lighthouseaccount](TESTING-screenshots/lighthouse-account.png) |
| Login | ![lighthouselogin](TESTING-screenshots/lighthouse-login.png) |
| Recipes | ![lighthouserecipes](TESTING-screenshots/lighthouse-recipes.png) |
| Individual Recipes - all the same | ![lighthouserecipe](TESTING-screenshots/lighthouse-recipe1.png) |

## Responsiveness
I've tested my deployed project on different screen sizes. I have also tried on laptop and desktop with no issues.

| Type | Screenshot | Notes |
| ---- | ---------- | ----- |
| Samsung Galaxy s8 | ![samsung](TESTING-screenshots/samsung-galaxys8.png) | Loaded as expected |
| Pixel7 | ![pixel](TESTING-screenshots/pixel7.png) | Too much whitespace |
| IPad Air | ![ipad](TESTING-screenshots/ipadair.png) | Loaded as expected |
| IPhone 14 Pro Max | ![iphone14](TESTING-screenshots/iphone14promax.png) | Loaded as expected |
| IPhone se | ![iphonese](TESTING-screenshots/iphonese.png) | Loaded as expected |

## Extra Testing

Once I deployed the site on Heroku, the images that worked on the local deloyed site, no longer worked when the site went live. I found out this was because I needed to have the images saved elsewhere and link it to my Heroku account.

I created a [AWS account](https://aws.amazon.com/), created a new bucket for Protein Bite and uploaded my images to that and linked it with Heroku. When relaunching, the images all now load. 

To test this still worked with the admin backend account, I created a test page and uploaded a test image and text in the text boxes. Since testing and getting the outcome I wanted, I have since deleted this test recipe.

![Recipe card test](TESTING-screenshots/test-recipe-screenshot.png)
![Indivdual recipe page test](TESTING-screenshots/test-recipepage-screenshot.png)
![Deleting test recipe](TESTING-screenshots/delete-test-recipe.png)

I have also done manual testing by clicking on all links and pages on multiple different browsers. I've also created a test account to make sure all the forms work with creating, managing and deleting user accounts.

| Test | Screenshot | Notes |
| ---- | ---------- | ----- |
|What happens when a user tries to create an account when a different user already has that username | ![username take](README-images/usernametaken.png) | Error comes up saying username already taken. |
| Delete user account | ![delete account](README-images/deleteaccount.png) | An extra warning appears to make sure the user is sure they want to delete their account. |
| What happens when you add a comment | ![comment section test](README-images/commentsectiontest.png) | Comment appears where expected; you can only add a comment in a user is signed in. |
| No image to upload | ![No recipe image](TESTING-screenshots/no-recipe-image.png) | If a recipe gets uploaded but no photos have been taken of the food yet, I wanted to check the picture coming soon image would take it's place. This can then be changed with the admin login when an image is available. This means there will never be a blank spot where an image should be, which will keep the layout correct and not make anything look like its missing. |
| Signing into an account with incorrect details | ![Incorrect login](TESTING-screenshots/incorrect-login.png) | A message appears to let the user know that they have entered incorrect details.  |
| Method & Ingredients Button | ![Method](TESTING-screenshots/method-screenshot.png) ![Ingredients](TESTING-screenshots\ingredients-screenshot.png) | When you go into a specific recipe it shows the ingredients first, with a buton above called Method. If you click the method button, it changes the information below from ingredients to the recipe method. It also changes the name of the button to which ever information it's not currently showing. Giving the user the option to click back and forth between ingredients and method in each recipe. |

