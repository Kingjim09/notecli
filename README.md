<h1 align="center">Note CLI</h1>

<p align="center">
  <img src="https://img.shields.io/badge/License-MIT-blue.svg" alt="License: MIT">
  <img src="https://img.shields.io/badge/notecli-0.4.0-yellow.svg" alt="NoteCLI Version">
</p>

<p><strong>NoteCLI</strong> is a <strong>command-line interface (CLI) note-taking tool</strong>. It's a simple, text-based program that runs in the terminal, allowing you to <strong>create</strong>, <strong>view</strong>, <strong>edit</strong>, and <strong>delete notes</strong>.</p>

<h2>Features</h2>
<ul>
  <li><strong>Navigate/View Files</strong>: Allows the user to navigate directories and view files.</li>
  <li><strong>Go Back to Parent Directory</strong>: Use the <code>go_back()</code> feature to easily return to a parent folder when navigating.</li>
  <li><strong>Edit Files</strong>: Enables the user to edit their files directly from the terminal.</li>
  <li><strong>Create Files</strong>: Easily create files from the terminal using intuitive prompts.</li>
  <li><strong>Create Folders</strong>: Effortlessly create folders to organize your notes and files.</li>
  <li><strong>Change Path</strong>: Allows the user to change their default path when launching the <code>NoteCLI</code>.</li>
  <li><strong>Improved Path & Config Handling</strong>: Now uses a consistent and safer approach for storing and validating the config path in <code>data.json</code>.</li>
  <li><strong>Store Data in JSON</strong>: Stores user data in <code>data.json</code>, so they don’t have to provide the same information repeatedly.</li>
  <li><strong>Delete Files/Folders</strong>: Quickly delete unwanted files or folders from the terminal with a confirmation prompt. Now includes better handling for non-existent paths.</li>
</ul>

<h2>Purpose</h2>
<p><code>NoteCLI</code> is designed to help users manage their notes and files in a terminal environment. It's perfect for those who prefer working in a text-based interface while keeping their note-taking simple and efficient.</p>

<h2>Pre-requisites</h2>
<p>Make sure you have Python 3.13.2 (or a compatible version) installed. You can check your Python version with the following command:</p>
<pre><code>python --version  # Expected output: Python 3.13.2</code></pre>

<p>If the command doesn't return anything or throws an error, you'll need to install Python. You can download it from the official site here: <a href="https://www.python.org/downloads/">python.org</a>.</p>

<h2>Installation</h2>
<ol>
  <li>Clone this repository to your local machine:
    <pre><code>git clone https://github.com/Kingjim09/notecli.git
cd notecli</code></pre>
  </li>
  <li>Install the required dependencies:
    <pre><code>pip install -r requirements.txt</code></pre>
  </li>
</ol>

<h2>Usage</h2>
<ol>
  <li>Run the <code>main.py</code> script:
    <pre><code>python src/main.py</code></pre>
  </li>
  <li>Follow the prompts to interact with the CLI and perform actions like creating, viewing, editing, or deleting notes.</li>
</ol>

<h2>LICENSE</h2>
<p>This project is licensed under the <a href="LICENSE">MIT License</a>. See the LICENSE file for more information.</p>
