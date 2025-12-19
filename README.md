# Role Based Login and Registraion Auth Flow

## Features Implemented

### User Authentication

- User **Registration & Login**
- Secure **Email OTP verification** during registration
- Password validation & confirmation
- JWT-based authentication

### Admin Authentication

- Separate **Admin Login**
- Secure admin authentication using access tokens
- Role-based navigation to admin dashboard

---

## UI / UX Enhancements

- Followed **design team–provided templates**
- Consistent **color palette and layout** across:
  - User Login
  - User Registration
  - Admin Login
- Split-screen layout:
  - **Left:** Illustration / visual section
  - **Right:** Authentication form
- Responsive design using **Tailwind CSS**
- Clean, modern UI with rounded cards and smooth spacing

---

## Tech Stack

### Frontend

- React.js
- Tailwind CSS
- React Router
- Axios

### Backend

- Python (FastAPI)
- JWT Authentication
- Email service for OTP delivery

---

## Project Structure (Simplified)

```bash
auth/
├── backend/
│   ├── app/
│   │   ├── main.py
│   │   ├── db.py
│   │   ├── models.py
│   │   ├── schemas.py
│   │   ├── auth.py
│   │   ├── routes/
│   │   │   ├── auth_routes.py
│   │   │   ├── admin_auth_routes.py
│   │   │   └── auth_otp_routes.py
│   │   └── utils/
│   │       └── email.py
│   ├── .env
│   └── requirements.txt
│
├── public/
│   └── images/
│
├── src/
│   ├── components/
│   │   ├── Login.jsx
│   │   ├── Register.jsx
│   │   └── AdminLogin.jsx
│   ├── services/
│   │   └── api.js
│   ├── App.jsx
│   ├── index.js
│   ├── index.css
│   └── App.css
│
├── .env
├── .gitignore
├── package.json
├── package-lock.json
├── postcss.config.js
├── tailwind.config.js
└── README.md
```

---

## Environment Variables

Create a `.env` file for sensitive configurations:

DATABASE_URL=your_backend_url

EMAIL_USER=your_email
EMAIL_PASSWORD=your_password
