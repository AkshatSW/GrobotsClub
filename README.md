# Contributing to Grobots Club Website

Welcome to the Grobots Website project! We're excited to have you contribute. Follow these steps to get started:

## Prepared by
- Akshat Srivastava
- Shanvi Shukla
- Anuj Dubey

## Prerequisites

Before you start contributing, make sure you have the following prerequisites in place:

1. **Create a New Virtual Environment and Activate It:**
   - Set up a new virtual environment to isolate your project dependencies:
     ```
     python3 -m venv grobots-env
     ```
   - Activate the virtual environment:
     - On Windows: `grobots-env\Scripts\activate`
     - On macOS and Linux: `source grobots-env/bin/activate`

2. **Install Python3 and Flask:**
   - Make sure you have Python 3.x installed on your system.
   - Install Flask using:
     ```
     pip install flask
     ```

3. **Install Required Dependencies:**
   - Navigate to the project directory and install the necessary dependencies:
     ```
     cd grobots-website  # Navigate to the project directory
     pip install -r requirements.txt
     ```

## How to Contribute

1. **Fork the Repository:**
   - Click the "Fork" button at the top-right of this repository's page to create your own fork.

2. **Clone the Repository:**
   - Clone your forked repository to your local machine:
     ```
     git clone <repository-url>
     ```

3. **Activate the Virtual Environment:**
   - Ensure that your virtual environment is activated:
     - On Windows: `grobots-env\Scripts\activate`
     - On macOS and Linux: `source grobots-env/bin/activate`

4. **Create a New Branch:**
   - Create a new branch for your changes:
     ```
     git checkout -b feature/new-feature
     ```
   - Choose a descriptive name like `feature/new-feature` or `bugfix/issue-number`.

5. **Make Changes:**
   - Make necessary changes to the website's code, content, or other relevant files.

6. **Commit Changes:**
   - Stage your changes:
     ```
     git add .
     ```
   - Commit your changes with a clear message:
     ```
     git commit -m "Add descriptive commit message"
     ```

7. **Push to Your Fork:**
   - Push your changes to your forked repository:
     ```
     git push origin feature/new-feature
     ```

8. **Create a Pull Request (PR):**
   - Visit the original repository.
   - Click "New Pull Request."
   - Set the base repository and branch to the main branch of Grobots Website.
   - Set the head repository and branch to your fork and the branch you created.
   - Write a descriptive title and comment for your pull request.
   - Click "Create Pull Request" to submit.

9. **Review and Discuss:**
   - Engage in the discussion about your PR.
   - Make any necessary changes based on feedback.

10. **Merge or Close:**
    - Once your PR is approved, a maintainer will merge it into the main branch.
    - Address feedback and update your branch if required.

11. **Sync with Upstream:**
    - Keep your fork up-to-date by syncing with the original project:
      ```
      git remote add upstream <original-repository-url>
      git fetch upstream
      git merge upstream/main
      ```

## Congratulations!
You've made a contribution to the Grobots Website project. Your efforts are now part of our open-source community.
