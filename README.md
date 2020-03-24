<p align="center">
<img src="https://i.imgur.com/Qsdgosd.jpg" alt="Smiley face" height="500" width="500">
</p>

[![Python3.7+](https://img.shields.io/badge/Python-3.7%2B-green.svg)](https://www.python.org/downloads)

## How to start

<b>Clone this repo:</b> ```git clone https://github.com/hersel91/nebula.git```
<br>

## Requirements ⚙️

Besides [Python 3.7+](https://www.python.org/downloads/) we will be using the following packages:

<b>Install requirements</b> (https://github.com/Infocom-Telegram-Community/nebula/blob/master/requirements.txt)
<br>
<b>Command:</b> ```pip install -r requirements.txt``` <b>Or</b> ```pip3 install -r requirements.txt```

<br>

## Global Commands List
<br>
<h3>Commands to be executed in response to a username</h3>
<br>
{text} = text to insert
<ul>
<li>/ban [ban uyser]</li>
<li>/muta [mute user]</li>
<li>/smuta [unmute user]</li>
<li>/info [user information and chat]</li>
<li>/delete [delete message]</li>
<li>/kick [kick user]</li>
<br>
<h3>Commands to be executed in chat</h3>
<li>/a {text} [announcement]</li>
<li>/listwelcome [watch your group welcome]</li>
<li>/setwelcome {text} [set the welcome]</li>
<li>/updatewelcome {text} [update the welcome]</li>
<li>/add BUTTONNAME,example.com [add welcome button]</li>
<li>/list [remove and see buttons]</li>
<li>/meteo cityname [weather]</li>
</ul> 

<b>Import the database from the /SQL folder</b>
<br>
<b>In your shell start this bot use this command=></b> ```python3 bot.py```

### Do you have problems installing mysqlclient requirements?
Use this command:
<ul>
<li><b>Centos:</b> sudo yum install mysql-devel</li>
<li><b>Ubuntu/Debian:</b> sudo apt-get install python-dev default-libmysqlclient-dev</li>
<li><b>Fedora:</b> sudo dnf install python python-devel mysql-devel redhat-rpm-config gcc</li>
</ul>

<b>Important Note: This bot only works with python telegram bot 12.1.1+</b>
<br>

## How can I create a plugin?
🔷 Go to the /plugins folder (https://github.com/Infocom-Telegram-Community/nebula/tree/master/plugins)
<br>
🔷 inside the plugins folder you will find the <code>__init__.py</code> file
    Every time you add a plugin inside the folder you have to add the name of the file in the __all__ array
    For example:
    if we create the banana.py file we have to insert banana inside __all__
    <a href="https://imgur.com/pMiwxIR"><img src="https://i.imgur.com/pMiwxIR.png" title="source: imgur.com" /></a>
    <a href="https://imgur.com/dR0nN1P"><img src="https://i.imgur.com/dR0nN1P.png" title="source: imgur.com" /></a>
    <br>
🔷Now let's go to bot.py and enter our plugin command with the following command line:
    dispatcher.add_handler (CommandHandler ("banana", plugins.banana.init))
    where we will insert plugins.filename.functionname
    and in "banana" enter the command that will work on telegram (/banana)
    <a href="https://imgur.com/sOoPruP"><img src="https://i.imgur.com/sOoPruP.png" title="source: imgur.com" /></a>
    <br>
🔷 Video Tutorial: https://youtu.be/Bmm37wG1EZQ

# Credits
<br>
Thanks to https://github.com/SteelManITA
<br>
Thanks to https://github.com/stefano-mecocci
<br>
Thanks to https://github.com/Kavuti/python-italy-telegram-bot

## License 📄

Please read the [LICENSE](LICENSE) provided in this rep