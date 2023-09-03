# EnglishForKids
This is a python application for smartphones that can teach small kids English language through both writing and speaking tasks.
The project has this pages:
a- Sign in page for logging in with exist accounts.
b- Sign up page for regestering new accounts.
c- Main page with three options:
 - <b>Writing Test</b> button : to enter the writing test page which contain the test picture, text feild, and answering button.
   if the input text is correct, score increase by 1 else wrong answer's value increasing by 1.
   if wrong answer's value reaches 3, the user loses.
 - <b>Speaking Test</b> button : to enter the speaking test page which contain the test picture, recording button, and answering button.
   when the user press recording button the system waits for the user's voice then converting it to text offline through vosk library.
   if the converted voice is correct, score increase by 1 else wrong answer's value increasing by 1.
   if wrong answer's value reaches 3, the user loses.
 - <b>Leadboard</b> page button : to enter scores page and show users names and scores.
<h2>Requirements:</h2>
1- python-telegram-bot version 20.3 to install it:
pip install python-telegram-bot==20.3
2- selenium library :
pip install selenium
3- Google Chrome browser version 114.0.5735.134 (stop the auto updating so that the Chrome version keep up with the Chromdriver version)
4- ChromeDriver 114.0.5735.90 you can download it from:
https://chromedriver.storage.googleapis.com/index.html?path=114.0.5735.90/
5- Pandas and CSV libraries:
pip install pandas
6- Telegram account and platform(App/Desktop/Web)
7- Creating Telegram bot using botFather and save the bot token.
8- A good network speed
