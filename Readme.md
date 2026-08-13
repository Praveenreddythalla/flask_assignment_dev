# Flask Voting Application

## Project Description

This project is a simple Flask web application that provides a basic voting system.

Users can:

* View the application welcome page
* Check the application health status
* Vote for candidates
* View the current vote counts
* Reset all stored votes

Voting information is stored temporarily in memory while the application is running.

## Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/Praveenreddythalla/flask_assignment_dev.git
cd flask_assignment_dev
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

### 3. Activate the Virtual Environment

For PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

### 4. Install Dependencies

```bash
pip install flask
```

### 5. Run the Application

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

### Workflow

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

The application welcome page is displayed when accessing the root endpoint.

![Welcome Screenshot](./Screenshots/Welcome.png.png)

### 2. Health Status

The health endpoint confirms that the application is running successfully.

![Health Status](./Screenshots/health.png.png)

### 3. Vote Recorded

A vote is recorded for the selected candidate using the voting endpoint.

![Vote Recorded](./Screenshots/votingapp.png.png)

### 4. Vote Results

The results endpoint displays the current vote count for the candidates.

![Vote Results](./Screenshots/votingresults.png.png)

### 5. Reset

The reset endpoint clears all stored vote counts.

![Reset](./Screenshots/votingreset.png.png)

## Git Commit History

The following command can be used to verify the evolution of the project from Version 1 to Version 2:

```bash
git log --oneline --graph --decorate main dev
```

The Git history demonstrates the development progression from Version 1 to Version 2 using the `dev` and `main` branches.

All screenshots are stored in the `Screenshots/` folder.
