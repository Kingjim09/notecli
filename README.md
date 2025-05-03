<h1 align="center">Note CLI</h1>

<p align="center">
  <img src="https://img.shields.io/badge/License-MIT-blue.svg" alt="License: MIT">
  <img src="https://img.shields.io/badge/notecli-0.7.0-yellow.svg" alt="NoteCLI Version">
</p>

<p><strong>NoteCLI</strong> is a <strong>command-line interface (CLI) note-taking tool</strong>. It's a simple, text-based program that runs in the terminal, allowing you to <strong>create</strong>, <strong>view</strong>, <strong>edit</strong>, and <strong>delete notes</strong>. Whether you're working on notes for school, personal projects, or just organizing your thoughts, NoteCLI offers a quick and efficient way to manage your files directly from the terminal.</p>

<h2>Features</h2>
<ul>
  <li><strong>Navigate/View Files</strong>: Navigate through directories and view files with ease.</li>
  <li><strong>Go Back to Parent Directory</strong>: Use the <code>..</code> command to return to a parent folder when navigating through directories.</li>
  <li><strong>Edit Files</strong>: Edit files directly from the terminal, making it easy to update and modify your notes.</li>
  <li><strong>Create Files</strong>: Create new files with customizable content and name directly from the terminal.</li>
  <li><strong>Create Folders</strong>: Organize your notes and files by creating folders in the current directory.</li>
  <li><strong>Change Path</strong>: Change the default working directory for the CLI tool, so you can set a new base directory for your notes.</li>
  <li><strong>Improved Path & Config Handling</strong>: Safely store and validate the config path using <code>data.json</code>, ensuring your preferences are securely saved.</li>
  <li><strong>Store Data in JSON</strong>: Automatically store user data in <code>data.json</code>, preventing the need to repeatedly enter the same information.</li>
  <li><strong>Delete Files/Folders</strong>: Delete files or folders with a confirmation prompt, along with improved handling for non-existent paths.</li>
  <li><strong>Improved User Input Handling</strong>: A more intuitive input system using <code>prompt_user_for_input()</code>, making the CLI more user-friendly.</li>
</ul>

<h2>Purpose</h2>
<p><code>NoteCLI</code> is designed to streamline the process of managing notes and files through a text-based interface. It's perfect for users who prefer working in the terminal while maintaining an organized and simple way to manage their note-taking system.</p>

<h2>Pre-requisites</h2>
<p>Make sure you have Python 3.13.2 (or a compatible version) installed. You can check your Python version with the following command:</p>
<pre><code>python --version  # Expected output: Python 3.13.2</code></pre>

<p>If you don't have Python installed, you can download it from the official site: <a href="https://www.python.org/downloads/">python.org</a>.</p>

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
  <li>Follow the prompts to interact with the CLI. You can perform actions like creating, viewing, editing, or deleting notes, navigating directories, and much more.</li>
</ol>

<h2>LICENSE</h2>
<p>This project is licensed under the <a href="LICENSE">MIT License</a>. See the LICENSE file for more information.</p>
