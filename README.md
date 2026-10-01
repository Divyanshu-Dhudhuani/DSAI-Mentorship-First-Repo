# DSAI Mentorship — Git & GitHub Assignment

## Introduction

This assignment is designed to give you hands-on practice with the basic Git and GitHub workflow, including:

- Forking and cloning repositories
- Creating and tracking files with Git
- Using `.gitignore`
- Creating and working with branches
- Making commits and pushing changes
- Creating and resolving merge conflicts
- Understanding which version of a file is retained during a conflict
- Rewriting Git history using `git rebase`
- Reverting an already-pushed change through history manipulation

You will work with the following repository:

**Repository:**  
https://github.com/ShlokDivyam1109/DSAI-Mentorship-First-Repo

Throughout this assignment, replace `<YOUR_NAME>` with your actual name.

---

## Task 1: Fork and Clone the Repository

First, fork the given repository to your own GitHub account.

After forking it, clone **your fork**, not the original repository, to your local machine.

### Hint: Use

```bash
git clone <YOUR_FORK_URL>
cd DSAI-Mentorship-First-Repo
```

Verify that the repository was cloned correctly using:

```bash
git remote -v
```

The `origin` remote should point to **your fork**.

---

## Task 2: Create Your Personal Folder

Inside the repository, create a folder using your name.

The structure should look like:

```text
DSAI-Mentorship-First-Repo/
└── <YOUR_NAME>/
```

All files belonging to your assignment must be placed inside this folder, except for the `.gitignore` file described later.

---

## Task 3: Create the Python Program

Inside `<YOUR_NAME>/`, create a Python file.

For example:

```text
<YOUR_NAME>/
└── main.py
```

The Python program must contain the following components:

### 1. A function to read `secret.txt`

Create a function that opens a file named:

```text
secret.txt
```

The file must contain exactly:

```text
Secret123
```

The function should read the password from the file and pass it to another function named:

```python
check(password)
```

### 2. The `check(password)` function

Create the function:

```python
def check(password):
```

**Do not write any code inside this function initially.**

The purpose of this assignment is to modify this function later on another Git branch.

### 3. The `main()` function

Create:

```python
def main():
```

`main()` must call the function responsible for reading the password from `secret.txt`.

### 4. Program entry point

At the very end of the Python file, include:

```python
if __name__ == '__main__':
    main()
```

Do not omit this section.

---

## Task 4: Create `secret.txt`

Inside your `<YOUR_NAME>` folder, create:

```text
secret.txt
```

Its contents must be exactly:

```text
Secret123
```

Your directory should now look approximately like:

```text
DSAI-Mentorship-First-Repo/
└── <YOUR_NAME>/
    ├── main.py
    └── secret.txt
```

---

## Task 5: Create the `.gitignore`

Create a `.gitignore` file **outside your name folder**, at the root of the repository.

The `.gitignore` must ignore:

```text
secret.txt
```

This means that Git should not track the password file.

Your structure should now look like:

```text
DSAI-Mentorship-First-Repo/
├── .gitignore
└── <YOUR_NAME>/
    ├── main.py
    └── secret.txt
```

### Hint: Use

```bash
echo secret.txt >> .gitignore
```

Then check:

```bash
git status
```

`secret.txt` should not appear as a file to be committed.

---

## Task 6: Commit and Push Your Initial Work

Add the required files to Git, commit them, and push them to your fork.

### Hint: Use

```bash
git add .
git commit -m "Add initial password checker"
git push origin main
```

Check your GitHub repository and verify that:

- Your `<YOUR_NAME>` folder exists.
- Your Python file is present.
- `.gitignore` is present.
- `secret.txt` is **not** present on GitHub.

---

## Task 7: Create `branch1`

Create a new branch named exactly:

```text
branch1
```

Switch to it.

### Hint: Use

```bash
git checkout -b branch1
```

Verify your current branch:

```bash
git branch
```

---

## Task 8: Modify the Password Checker in `main`

Return to the `main` branch.

In your Python file, modify the `check(password)` function so that it returns:

```python
password == "Secret123"
```

Do not change the other required parts of the program.

Commit this change and push it to GitHub.

### Hint: Use

```bash
git checkout main
git add .
git commit -m "Implement password checking"
git push origin main
```

At this stage, `main` contains the password-checking implementation.

---

## Task 9: Make a Different Change in `branch1`

Switch back to:

```text
branch1
```

```bash
git checkout branch1
```

Now modify your Python program so that the filename being accessed changes from:

```text
secret.txt
```

to:

```text
password.txt
```

The filename must also be changed in `.gitignore`.

Therefore, `.gitignore` on `branch1` must ignore:

```text
password.txt
```

instead of:

```text
secret.txt
```

Commit and push this change.

### Hint: Use

```bash
git add .
git commit -m "Change password file name"
git push origin branch1
```

---

## Task 10: Merge `branch1` into `main`

Switch to `main`:

```bash
git checkout main
```

Now merge `branch1` into `main`:

```bash
git merge branch1
```

A **merge conflict should occur** because both branches have modified the same Python file in different ways.

You must manually resolve this conflict.

### Required resolution

When resolving the conflict, make the version from **`branch1` prevail**.

In other words, the changes made in `branch1` should overwrite the conflicting version from `main`.

### Hint: You may use

```bash
git checkout --theirs <filename>
```

Then stage the resolved file:

```bash
git add .
```

Complete the merge:

```bash
git commit
```

Verify that the merge was successful using:

```bash
git status
```

---

## Task 11: Add the Password Comment

After successfully resolving the merge, add the following comment to the Python file:

```python
#Password is Secret123
```

Commit this change and push it to `main`.

### Hint: Use

```bash
git add .
git commit -m "Add password comment"
git push origin main
```

The comment should now be part of the latest commit.

---

## Task 12: Rewrite Git History Using Rebase

Now use Git to remove/rewrite the latest commit containing:

```text
Add password comment
```

Use an interactive rebase to remove that commit from the local history.

### Hint

First inspect the recent commit history:

```bash
git log --oneline
```

Then use:

```bash
git rebase -i HEAD~2
```

In the interactive editor, remove/drop the commit that added:

```text
#Password is Secret123
```

After the rebase, verify the history:

```bash
git log --oneline
```

The `Add password comment` commit should no longer appear in the local branch history.

---

## Task 13: Force Push the Rewritten History

Since you have rewritten commits that were already pushed to GitHub, a normal push will be rejected.

Force push the rewritten `main` branch.

### Hint: Use

```bash
git push --force-with-lease origin main
```

Verify the commit history on GitHub.

---

## Expected Final Repository Structure

Your repository should approximately contain:

```text
DSAI-Mentorship-First-Repo/
├── .gitignore
└── <YOUR_NAME>/
    └── main.py
```

Remember that:

- `secret.txt` should be ignored.
- `password.txt` should also be ignored on `branch1`.
- The final `main` history should no longer contain the commit that added `#Password is Secret123`.
- The merge between `main` and `branch1` must have produced and resolved a conflict.

---

## Git Commands You Should Practice

By completing this assignment, you should have used commands such as:

```bash
git clone
git remote
git status
git add
git commit
git push
git checkout
git branch
git merge
git log
git rebase
git push --force-with-lease
```

The objective is not merely to reach the final state. You should understand **why** each command is being used and what changes it makes to the Git history.
