# EnglishForKids
This is a python application for smartphones that can teach small kids English language through both writing and speaking tasks.<br>
The project has this pages:<br>
a- Sign in page for logging in with exist accounts.<br>
b- Sign up page for regestering new accounts.<br>
c- Main page with three options:<br>
 - <b>Writing Test</b> button : to enter the writing test page which contain the test picture, text feild, and answering button.
   if the input text is correct, score increase by 1 else wrong answer's value increasing by 1.
   if wrong answer's value reaches 3, the user loses.
 - <b>Speaking Test</b> button : to enter the speaking test page which contain the test picture, recording button, and answering button.
   when the user press recording button the system waits for the user's voice then converting it to text offline through vosk library.
   if the converted voice is correct, score increase by 1 else wrong answer's value increasing by 1.
   if wrong answer's value reaches 3, the user loses.
 - <b>Leadboard</b> page button : to enter scores page and show users names and scores.
<h2>Requirements:</h2>
1- Kivy library, to install it:<br>
pip install kivy<br>
2- Vosk library :<br>
pip install vosk<br>
3- Pygame library:<br>
pip install pygame<br>
4- Pandas and CSV libraries:<br>
pip install pandas
