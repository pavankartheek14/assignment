# Assignment Project

##  Overview
This project is a React-based assignment that demonstrates form handling, state management React concepts without any backend integration.

---

##  What I Implemented
- A React application using **functional components**
- Form to input:
  - Model Name
  - Domain (NLP, CV, or Tabular)
- Used **React state (`useState`)** to manage form data
- Displayed submitted models dynamically in a list
- Proper component structure and reusable components
- Clean UI which is imported from bootstarp


In the project directory, you can run:

### `npm start`

Runs the app in the development mode.\
Open [http://localhost:3000](http://localhost:3000) to view it in your browser.

The page will reload when you make changes.\
You may also see any lint errors in the console.

### `npm run build`

Builds the app for production to the `build` folder.\
It correctly bundles React in production mode and optimizes the build for the best performance.

The build is minified and the filenames include the hashes.\
Your app is ready to be deployed!

## Screen Shots of UI

<img width="1432" height="813" alt="Screenshot 2025-12-28 at 3 22 10 PM" src="https://github.com/user-attachments/assets/9403ac43-ee1e-4290-bc29-106e9872f84f" />
<img width="1417" height="840" alt="Screenshot 2025-12-28 at 3 21 39 PM" src="https://github.com/user-attachments/assets/4183d758-ca33-4a38-8a3e-a5310f8f6c17" />
<img width="1432" height="825" alt="Screenshot 2025-12-28 at 3 20 50 PM" src="https://github.com/user-attachments/assets/ae231002-9649-424c-ab9b-71488072fcbc" />

## State Flow and Component Structure

The application uses React functional components with the useState hook for state management. Form inputs are controlled using local state and updated on every user input. On submission, the entered data is stored in an array state and the form is reset. React automatically re-renders the UI to display the updated list of submissions. The App component serves as the root component and renders the main Text component, keeping the structure modular and clean.

