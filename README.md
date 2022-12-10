# The Fitness Lab


## Site Overview

[Live Site Link](https://thefitnesslab.herokuapp.com/)

![Site Overview]()





## Planning

### Agile Approach
This project was implemented using an Agile approach to take advantage of the iterative and incremental development.

A key advantage of this approach was the iterative and incremental development, which created a highly adaptable and efficient work schedule. Tasks were completed in stages to fulfil user stories, which incrementally improved the functionality of the website. The project was split into two-day iterations, to review progress and adjust the work schedule accordingly.

GitHub Projects was used to organise the project tasks and timeline. A kanban board was used to move user stories across To Do, In Progress and Done columns according to their status.

![Kanban]()



### Data Model
* This project used Object Oriented programming, utilising model classes to define data.
* PostgreSQL was used to create a relational database of objects
* Four classes were defined: *****************User, Country, Article and Comment*****************
* Data fields were defined for each parameter
* Foreign key fields were used to reference objects in different tables

![Database model](readme_images/database_model.png)







## Future Enhancements
Various additional features would bring a greater user experience to the website:
* Allow only users who have bought items to give items reviews and ratings.
* Allow users to interactively add a rating to the products.
* Add a sale and deals section and have the first products a customer see be items on sale.
* Add a wishlist so users can add products which they would like to buy in the future to.
* Add a related products section where users can see similar products to the one they are currently viewing.





## Marketing

A Facebook page was created to help generate business for the site and to raise awareness of the brand.

Using organic social media will be a key way in developing the business. The aim is to have a presence on other social media sites such as Twitter, Instagram and LinkedIn as these are the main social media channels young adult men would use.

Using paid social media will also be a key target as focussing on advertising to users who have already visited the site will increase revenue. This can cost a significant amount but, when used correctly and intentionally, in the long term it will produce good results.

Email marketing will be a key part in increasing website traffic where The newsletter sign-up is the first stage of retrieving emails.

Using paid adverts such as Google ads will not initially be a priority due to the cost but will be in the future.






## Technology Used

### Languages
* HTML - Creating and adding content
* CSS - Styling content
* [JavaScript](https://www.javascript.com/) - Manipulating DOM content
* [Python 3](https://www.python.org/downloads/) - Backend code for writing classes methods and functions.

### Extensions
* [Django](https://www.djangoproject.com/) - Full stack framework with convenient shortcuts for effective website backend. Allauth and Coverage extensions were also used for users authentication and testing code coverage respectively.
    * [django-allauth](https://django-allauth.readthedocs.io/en/latest/index.html) - used to handle the site users' accounts, including sign up, login and logout features.
    * [django-crispy-forms](https://django-crispy-forms.readthedocs.io/en/latest/) - used for additional formatting and functionality of the site forms
    * [django-countries](https://pypi.org/project/django-countries/) - used to btaining a list of countries for customers to select at the checkout form
    * [django-storages](https://django-storages.readthedocs.io/en/latest/) - used to connect to Amazon S3 for storing the site's static and media files
* [Stripe](https://stripe.com/) - API used to confirm and handle customer payments
* [ElephantSQL](https://www.elephantsql.com/) - Database integrated with Heroku
* [Bootstrap](https://getbootstrap.com/) - Website structure and styling
* [jQuery](https://jquery.com/) - Implement javascript easily through the jQuery syntax
* [Font Awesome](https://fontawesome.com/v5.15/icons/) - Font icons

### Development & Deployment
* [Heroku](https://www.heroku.com/home) - Site deployment
* [Amazon S3](https://aws.amazon.com/s3/) - Storage of all media and static files for the deployed site on Heroku
* [GitPod](https://www.gitpod.io/) - IDE for local development
* [GIT](https://git-scm.com/) - Version Control
* [GitHub](https://github.com/) - to host the repositories for this project and the live website preview





## Testing
### Validator Testing
* HTML
    * No errors were found when running the HTML code through the [official W3C validator](https://validator.w3.org/)
* CSS
    * No errors were found when running the CSS code through the [official W3C Jigsaw validator](https://jigsaw.w3.org/css-validator/)
* JavaScript
    * No errors were found when running the JavaScript code through the [JSHint validator](https://jshint.com/).
* Python
    * No errors were found when running the Python code through the [PEP8 online validator](http://pep8online.com/).
* Accessibility
    * A high level of accessibility was returned when Lighthouse was ran in Google Chrome developer tools

### Flake8 Linting Errors
* All linting errors returned by flake8 were fixed to ensure that the code was written to the *** python standard.
* Linting errors within <code>.vscode/arctictern.py</code> as this was predefined code and in the <code>migrations</code> folders in all apps were ignored as this was system generated code.
* An error in the <code>checkout/apps.py</code> file saying that <code>'checkout.signals' imported but unused</code>. However, this is imported during runtime and is used within other files, therefore this error was ignored.


### Unfixed Bugs
* No known bugs have been left unfixed


## Development

### Cloning the Repository

  * Navigate to the main page of this repository
  * Click on the 'Code' dropdown menu to the left of the green 'Gitpod' button.
  * Copy the 'HTTPS url' and then open your own workspace.
  * Go to the terminal of the new workspace and type `git clone` + 'HTTPS url'.
  * Move all the files within the 'fitness_lab' folder into the route directory and delete the empty 'fitness_lab' folder.
  * To install all of the required modules use `pip3 install -r requirements.txt` in the terminal.
  * Type `python manage.py runserver` to run the site.
  * Next, migrate the changes to integrate them to the new database. Add both of the below statements to the terminal:
    * `python3 manage.py makemigrations`
    * `python3 manage.py migrate`
  * To get access to the Django Admin Panel type the below to the terminal and fill in the details:
    * `python3 manage.py createsuperuser` 
  * Finally, add an `env.py` file similar to the below:
```
  import os
  os.environ['DEVELOPMENT'] = 'True'
  os.environ['SECRET_KEY_TFL'] = 'enter_secret_key'
  os.environ['STRIPE_PUBLIC_KEY'] = 'enter_stripe_public_key'
  os.environ['STRIPE_SECRET_KEY'] = 'enter_stripe_secret_key'
  os.environ['STRIPE_WH_SECRET_TFL'] = 'enter_stripe_webhook_secret'`
```

### Integrating Stripe
  * Login to Stripe and sign up for free.
  * To retrieve the stripe STRIPE_PUBLIC_KEY and STRIPE_SECRET_KEY, when first loging in to stripe if, click on the 'Developers' tab and then click on the 'API Key' tab. Both keys can be copied from here.
  * To set up a webhook, first click on the 'Webhooks' tab in the 'Developers' tab
  * Click on 'Add Endpoint' and add the 'home page url' + '/checkout/webhook' similar to https://thefitnesslab.herokuapp.com/checkout/webhook/
  * Click 'Add Endpoint' and click 'Select all events'
  * Retrieve the 'STRIPE_WH_SECRET_TFL' by clicking 'Reveal' on the 'Signing section' of the webhook dashboard.

### Deploying to Heroku
  * Create a 'Procfile' with the following in it making sure to add in the application name: `web: gunicorn fitness_lab.wsgi:application`
  * Login to Heroku on their website and create a new app.
  * Click on the 'Resources' tab and add 'Heroku Postgres' to the Add*ons section.
  * Navigate to the 'Settings' tab in Heroku and click on the 'Reveal Config Vars' section and add in the below config vars:

|**Environment Variable**|**Value**                                           |
|------------------------|------------------------------------------------    |
| AWS_ACCESS_KEY_ID      | Access key provided by AWS                         |
| AWS_SECRET_ACCESS_KEY  | Secret key provided by AWS                         |
| DATABASE_URL           | Automatically Generated by Postgres                |
| EMAIL_HOST_PASSWORD    | Password for the address that sends out emails     |
| EMAIL_HOST_USER        | Email address for sending out emails               |
| SECRET_KEY             | Django secret key                                  |
| STRIPE_PUBLIC_KEY      | Publishable Key provided by Stripe                 |
| STRIPE_SECRET_KEY      | Secret Key provided by Stripe                      |
| STRIPE_WEBHOOK_SECRET  | Webhook Signing Secret provided by Stripe          |
| USE_AWS                | True                                               |
| DISABLE_COLLECTSTATIC  | 1                                                  |

  * Add in the correct 'ALLOWED_HOSTS' urls to settings.py
  * Now login to Heroku in the terminal of your workspace using `heroku login *i`
  * Type `heroku git:remote -a heroku_app_name` into your terminal then `git push heroku main`. This will deploy your app.
  * To migrate the databases to the Heroku Postgres database enter the below statements to your workspace terminal:
    * `heroku run python3 manage.py makemigrations`
    * `heroku run python3 manage.py migrate`

### Set-up Amazon S3
  * Once you're signed into Amazon AWS, navigate to S3 and create a new bucket.
  * In the permissions tab within your bucket add the below to the CORS configuration:

```
[
  {
    "AllowedHeaders": [
      "Authorization"
    ],
    "AllowedMethods": [
      "GET"
    ],
    "AllowedOrigins": [
      "*"
    ],
    "ExposeHeaders": []
  }
]
```
  * Click on 'Policy generator' under the Bucket Policy Tab and add in the ARN + `/*` (which looks similar to `arn:aws:s3:::your-bucket-name/*`) to the generated policies 'Resource' section. Then add the generated policy to the 'Bucket Policy Editor'.
  * Now navigate to the AWS app 'IAM' and create a 'Group' making sure you add in your existing S3 Bucket details.
  * Once you have done this, create a 'New Policy' and 'New User' and add them to your 'Group'.
  * After this, go back to the config variables in the Heroku app and delete the 'DISABLE_COLLECTSTATIC' variable.
  * Deploy again to heroku by entering `git push heroku main` in your terminal and you should be fully set up.



## Credits

### Content
  * [Django Documentation](https://docs.djangoproject.com/en/4.0/)
  * [Stripe Documentation](https://stripe.com/docs)
  * [Amazon S3 Documentation](https://docs.aws.amazon.com/s3/index.html)

### Media
  * [JD Sports](https://www.jdsports.co.uk/) - used for all product images and information.
  * [Pexels](https://www.pexels.com/) -  used for site photos excluding product images.
