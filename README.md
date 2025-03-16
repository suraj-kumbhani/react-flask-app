# =================== React Application ===================

## Available Scripts
In the project directory, you can run:
### `npm start`
Runs the app in the development mode.\
Open [http://localhost:3000](http://localhost:3000) to view it in your browser.

The page will reload when you make changes.\
You may also see any lint errors in the console.

### `npm test`
Launches the test runner in the interactive watch mode.\
See the section about [running tests](https://facebook.github.io/create-react-app/docs/running-tests) for more information.

### `npm run build`
Builds the app for production to the `build` folder.\
It correctly bundles React in production mode and optimizes the build for the best performance.

The build is minified and the filenames include the hashes.\
Your app is ready to be deployed!

See the section about [deployment](https://facebook.github.io/create-react-app/docs/deployment) for more information.

# =================== Python Application ===================

## Checkout to api directory
### `cd api`
The directory api has python application

## Create Virtual Environment
### `python -m venv venv`
It will start python virtual Environment So pyton application can be ran in separate Environment.

## Activate Virtual Environment
### `source venv/Scripts/activate`
It will start virtual Environment 
You can look for the name of your virtual environment within parentheses just before your command prompt it will have `(venv)` at the start of the Username 
### Example: `(venv) TestUser@DESKTOP-TREJSB MINGW64 /react-flask-app/api`

## install required Python tools/Libraries
### `pip install flask python-dotenv scikit-learn nltk bs4`
It will install all required python libraries which are used in this application

## To start the Python Application
### `flask run`
Runs the app in the development mode.\
It will run the App on [http://127.0.0.1:5000](http://127.0.0.1:5000).

# =================== API Use case ===================

## Time Endpoint 
### `/time`
It will return the current time.

## Summary Endpoint 
### `/summary`
Need to pass a Json with the key url and any article/blog url as value 
## Example
### `{ url: "https://docs.python.org/3/tutorial/index.html" }`
It will retun the title and description of the url we have sent in the API request body.


