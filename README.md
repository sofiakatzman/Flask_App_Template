#### How to run this in Development (Hosted in Backend Server)

##### Enter Pipenv Shell
pipenv shell

##### Install Python dependencies using Pipenv
pipenv install

##### Install Node.js dependencies for the client-side
npm install --prefix client

##### Build the client-side application for production
npm run build --prefix client

##### Navigate to the server directory
cd server

##### Apply database migrations 
flask db upgrade head

##### Seed the database with initial data
python seed.py

##### Start the Flask server for the backend 
python app.py

#### How to run this locally:

##### Start the client-side application (Frontend Server)
npm start --prefix client

##### Start the Flask Server (Backend Server)
python server/app.py

