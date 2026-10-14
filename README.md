# HTML/PHP Editor with Live Browser Preview

A lightweight desktop code editor developed using Python and Tkinter. This application helps beginners write, edit, save, and preview HTML and PHP files on a Windows computer.

It is designed for students, teachers, and beginner web developers who want a simple environment to practice web programming without using a complex code editor.

## ✨ Features

- **Simple Code Editor:** Write and edit HTML and PHP source code in a desktop text editor.
- **Open Existing Files:** Open files from the computer using a file selection dialog.
- **Save Code:** Save your work as HTML, PHP, or other text files.
- **HTML Preview:** Open saved HTML files directly in your default web browser.
- **PHP Preview with XAMPP:** Open PHP files through a local XAMPP web server.
- **Language Selection:** Switch the editor label between HTML and PHP.
- **UTF-8 File Support:** Read and write files using UTF-8 encoding.
- **Offline HTML Development:** Write and preview local HTML pages without an internet connection.

## 🛠️ Technologies Used

- Python
- Tkinter — desktop graphical user interface
- Python `os` module — file and directory management
- Python `webbrowser` module — opening browser previews
- Python `subprocess` module — imported for process management
- XAMPP — required to execute PHP files locally

## 💻 Requirements

- Windows computer
- Python 3 installed
- Tkinter support (usually included with standard Windows Python installations)
- A modern web browser
- XAMPP installed and Apache running for PHP preview

HTML preview works without XAMPP. PHP preview requires a correctly configured local PHP server.

## 🚀 Installation

### 1. Install Python

Download Python from:

https://www.python.org/downloads/

During installation, enable the option to add Python to PATH.

### 2. Download this project

Clone the repository:

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

Alternatively, download the repository as a ZIP file and extract it.

### 3. Run the application

Open Command Prompt in the project folder and execute:

```bash
python editorhtml.py
```

The HTML/PHP Editor window should open.

No additional Python packages are required by the current source code, provided Tkinter is available.

## 📖 How to Use

### Step 1: Select a language

Choose HTML or PHP from the language selection menu.

### Step 2: Write your code

Type your HTML or PHP source code into the editor area.

Example HTML program:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>My First Webpage</title>
</head>
<body>
    <h1>Welcome to Web Development</h1>
    <p>This page was created using Python HTML/PHP Editor.</p>
</body>
</html>
```

### Step 3: Save your file

Click **Save**, choose a location, enter a filename, and save it with the `.html` extension.

Example:

`index.html`

### Step 4: Preview your webpage

Click **Preview**. The application saves the current editor contents into its configured test directory and opens the HTML file in your browser.

### Step 5: Practice PHP

Install XAMPP and start Apache. Save a PHP file, for example `hello.php`, and use Preview to open it through the local server.

Example PHP program:

```php
<?php
echo "Hello, World!";
?>
```

The configured PHP preview address is:

`http://localhost/test/hello.php`

The PHP file must be present in the configured XAMPP test directory for this URL to work.

## 📁 Project Structure

```text
HTML-PHP-Editor/
├── editorhtml.py
└── README.md
```

The application creates the configured test directory when required:

```text
C:\xampp\htdocs\test
```

## 🎓 Educational Use Cases

This project can help students and teachers:

- Learn the fundamentals of HTML.
- Practice writing simple PHP programs.
- Understand the relationship between source code and browser output.
- Create small web pages and classroom demonstrations.
- Explore how local web development works.
- Develop introductory programming skills.

## ⚠️ Current Limitations

This is an introductory editor, not a full-featured IDE.

- No syntax highlighting or automatic code completion.
- No built-in error detection or debugging.
- No automatic formatting or indentation.
- PHP preview depends on XAMPP and correct file placement.
- The preview directory is hard-coded to `C:\xampp\htdocs\test`.
- The current application does not automatically save changes when the window closes.
- File extensions are not automatically validated against the selected language.
- The editor does not provide a live preview while typing.

For PHP execution, configure XAMPP and the preview directory correctly before use.

## 🔮 Future Improvements

Possible enhancements include:

- Syntax highlighting for HTML, CSS, JavaScript, and PHP.
- Line numbers and automatic indentation.
- Code completion and error messages.
- Integrated terminal and PHP error reporting.
- Customizable project and preview directories.
- Dark mode and adjustable font sizes.
- Split-screen editor and browser preview.
- AI-assisted code explanation and debugging.
- Automatic saving and recent-file history.

## 🤝 Contributing

Students, teachers, and developers are welcome to suggest improvements, report bugs, and contribute features.

Please test proposed changes before using them in a classroom or production environment.

## 📄 License

No license is currently specified. Add an appropriate open-source license, such as the MIT License, if you intend to allow others to reuse, modify, and distribute this project.

## 👨‍💻 Project Summary

A beginner-friendly Python desktop application for writing, saving, and previewing HTML and PHP programs, created to support practical web development learning.
