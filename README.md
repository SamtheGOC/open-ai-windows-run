<html>
<head>
	
</head>
<body>
	<h1>AI Buddy</h1>
	<p>AI Buddy is a tool that allows you to generate responses to your queries using the OpenAI Chat GPT-3 model. Simply press the <code>ctrl+alt+a</code> hotkey, paste your query in the pop-up window, and press the "Submit" button to generate a response. The response will be copied to your clipboard and a notification will be displayed.</p>
	<h2>Prerequisites</h2>
	<ul>
		<li>Python 3.7 or later</li>
		<li><code>openai</code> and <code>pyperclip</code> python packages</li>
		<li><code>plyer</code> package for notifications (optional)</li>
	</ul>
	<h2>Setup</h2>
	<ol>
		<li>Install the required packages:
			<pre>pip install openai pyperclip plyer</pre>
		</li>
		<li>Set your OpenAI API key:
			<pre>openai.api_key = "YOUR_API_KEY"</pre>
		</li>
		<li>Run the script:
			<pre>python ai_buddy.py</pre>
		</li>
	</ol>
	<h2>Usage</h2>
	<p>Press the <code>ctrl+alt+a</code> hotkey to open the pop-up window. Paste your query in the text box and press the "Submit" button. The response will be copied to your clipboard and a notification will be displayed.</p>
	<h2>Notes</h2>
	<ul>
		<li>The pop-up window can be resized and moved like any other window.</li>
		<li>The response may be truncated in the notification if it exceeds 256 characters.</li>
	</ul>
	<h2>Credits</h2>
<ul>
	<li><a href="https://openai.com/">OpenAI</a> for the Chat GPT-3 model</li>
	<li><a href="https://pypi.org/project/pyperclip/">pyperclip</a> for clipboard functionality</li>
	<li><a href="https://pypi.org/project/plyer/">plyer</a> for notification functionality (optional)</li>

