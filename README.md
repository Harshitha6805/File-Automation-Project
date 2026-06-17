# File Automation Project

## Description

The **File Automation Project** is a Python-based automation tool that performs various file management operations automatically. The main purpose of this project is to reduce manual effort by organizing, renaming, and deleting files efficiently.

The application automatically sorts files based on their extensions and moves them into appropriate folders. It also provides user input support, handles errors using exception handling, and records all performed operations using logging.

This project demonstrates the practical implementation of Python file handling, automation, operating system interaction, and logging concepts.

---

## Objective

The main objectives of this project are:

- To automate repetitive file management tasks.
- To organize files automatically based on their file extensions.
- To perform file renaming and deletion operations.
- To implement exception handling for error management.
- To maintain a record of all file operations using log files.
- To provide an easy-to-use command-line interface for users.

---

## Features

### 1. File Sorting

The program automatically sorts files into different folders based on their extensions.

Examples:

- `.jpg`, `.jpeg`, `.png` files → **Images Folder**
- `.pdf`, `.txt`, `.docx` files → **Documents Folder**

---

### 2. File Renaming

The application allows users to rename files by providing the existing file name and the new file name.

---

### 3. File Deletion

Users can delete unwanted files using the automated deletion option.

---

### 4. User Input Support

The program provides a menu-driven interface where users can select the required operation.

Available operations:

1. Organize Files
2. Rename Files
3. Delete Files

---

### 5. Exception Handling

The project uses exception handling to manage errors such as:

- Invalid file paths
- Missing files
- Duplicate file names
- Permission errors

This prevents the program from crashing during execution.

---

### 6. Operation Logging

All performed file operations are recorded in a log file named:

```
operation_logs.txt
```

The log file helps users track the activities performed by the automation script.

Example:

```
sample.txt moved to Documents
image.jpg moved to Images
```

---

# Technologies Used

## Python

Python is used as the main programming language for developing the automation script.

## OS Module

The OS module is used to interact with the operating system and perform file-related operations such as:

- Checking file paths
- Accessing directories
- Managing files and folders

## Shutil Module

The Shutil module is used for high-level file operations such as moving files from one folder to another.

## Exception Handling

Python exception handling using `try` and `except` blocks is used to handle runtime errors.

## Logging Module

The logging module is used to create and maintain operation logs.

---

# Project Structure

```
File-Automation-Project/

│
├── Documents/              # Stores sorted document files
│   ├── report.pdf
│   └── sample.txt
│
├── Images/                 # Stores sorted image files
│   └── image.jpg
│
├── automation.py           # Main Python automation script
│
├── README.md               # Project documentation
│
└── .gitignore              # Ignored files configuration
```

---

# How to Run

## Step 1: Clone the Repository

```bash
git clone https://github.com/Harshitha6805/File-Automation-Project.git
```

---

## Step 2: Navigate to Project Directory

```bash
cd File-Automation-Project
```

---

## Step 3: Run the Python Script

```bash
python automation.py
```

---

## Step 4: Select Operation

After running the program, select the required option:

```
===== FILE AUTOMATION SYSTEM =====

1. Organize Files
2. Rename File
3. Delete File

Enter your choice:
```

---

# Sample Execution

### Input

```
Enter your choice: 1

Enter folder path: Test_Files
```

### Output

```
File sorting completed successfully.
Files moved to respective folders.
```

---

# Logging Output

All operations performed by the program are stored in:

```
operation_logs.txt
```

Example log:

```
report.pdf moved to Documents
sample.txt moved to Documents
image.jpg moved to Images
```

---

# Advantages

- Reduces manual file organization work.
- Saves time by automating repetitive tasks.
- Provides accurate file management.
- Maintains records using logs.
- Easy to understand and modify.

---

# Future Enhancements

The project can be improved by adding:

- Graphical User Interface (GUI)
- Automatic scheduling of file operations
- Cloud storage integration
- Duplicate file detection
- Advanced file searching options

---

# Conclusion

The **File Automation Project** successfully automates common file management operations using Python. It organizes files, performs file operations based on user requirements, handles errors efficiently, and maintains operation records through logging.

This project demonstrates the use of Python automation concepts and provides a practical solution for managing files effectively.

---

# GitHub Repository

Repository Link:

https://github.com/Harshitha6805/File-Automation-Project