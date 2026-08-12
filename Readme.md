# Flask Voting Application

## Project Description

This project is a simple Flask web application that provides a basic voting system. Users can vote for candidates, view the current vote counts, check the application health, and reset all stored votes. Voting information is stored temporarily in memory while the application is running.

## Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/Praveenreddythalla/flask_assignment_dev.git
cd flask_assignment_dev
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the virtual environment

PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

### 4. Install dependencies

```bash
pip install flask
```

### 5. Run the application

```bash
python app.py
```

The application will be available at:

```text
http://localhost:5000
```

## API Endpoint Reference

| Endpoint       | Method | Description                                       |
| -------------- | ------ | ------------------------------------------------- |
| `/`            | GET    | Displays the welcome message                      |
| `/health`      | GET    | Checks whether the application is running         |
| `/vote/<name>` | GET    | Records one vote for the specified candidate      |
| `/results`     | GET    | Returns the current vote count for all candidates |
| `/reset`       | GET    | Clears all stored vote counts                     |

## Git Workflow

This project uses two Git branches:

* `dev` — Used for development work.
* `main` — Contains the stable version of the application.

Workflow:

```text
        Development
             ↓
            dev
             ↓
       Test the feature
             ↓
       Feature complete
             ↓
       Merge dev → main
             ↓
       Stable release
```

Version 1 was developed and tested in `dev` before being merged into `main`.

Version 2 was developed on top of Version 1 in `dev`, tested, and then merged into `main`.

No application development was performed directly on `main`.

## Version History

| Version   | Features                                           |
| --------- | -------------------------------------------------- |
| Version 1 | Flask application with `/` and `/health` endpoints |
| Version 2 | Added `/vote/<name>`, `/results`, and `/reset`     |

## Screenshots

### 1. Application Running

Welcome and health check.

### 2. Voting App

Vote, results, and reset functionality.

### 3. Git History

To verify the evolution from Version 1 to Version 2:

```bash
git log --oneline --graph --decorate main dev
```

Screenshots are stored in the `Screenshots/` folder.

### Welcome Screenshot

![Welcome Screenshot](Screenshots/WelcomePage.png)

### Health Status

![Health Status](Screenshots/HealthStatus.png)

### Vote Recorded

![Vote Recorded](Screenshots/BhargaviVote.png)

### Vote Results

![Vote Results](Screenshots/ResultVote.png)

### Reset

![Reset](Screenshots/ResetVote.png)

### Git Commit History

![Git Commit History](Screenshots/CommitHistory.png)