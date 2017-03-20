# Documentation

### API (server)

API Base URL: [https://serene-inlet-28321.herokuapp.com/api](https://serene-inlet-28321.herokuapp.com/api/people)

| method        | endpoint           | purpose  |
|:--------------|:--------------|:------|
|GET     | /people | Get all people |
| POST     | /people     |   Create a person |
| GET | /people/{id}     |  Get a person|
| PUT    | /people/{id}  | Edit a person|
| DELETE    | /people/{id}     |   Remove a person |

Note: The API returns JSON objects.

### Web App (client)

The page layout is as follows...

* [Index](https://serene-inlet-28321.herokuapp.com/) - lists all people
* [Detail](https://serene-inlet-28321.herokuapp.com/people/2) - person detail page
* [New](https://serene-inlet-28321.herokuapp.com/people/new/) - form to create a person
* [Edit](https://serene-inlet-28321.herokuapp.com/people/edit/2) - form to edit a person

All communication with the database is handled by the API. The Django web client makes requests to the API via service objects called by the views, which then render their specified template once JSON is returned. I separated the business logic and the request logic, so that the app would be more flexible to API changes in the future.
