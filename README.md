# EnglishForKids
This is a python application for smartphones that can teach small kids English language through both writing and speaking tasks.
The project has this pages:
a- Sign in page for logging in with exist accounts.
b- Sign up page for regestering new accounts.
c- Main page with three options:
 - Writing Test button : to enter the writing test page which contain the test picture, text feild, and answering button.
   if the input text is correct, score increase by 1 else wrong answer's value increasing by 1.
   if wrong answer's value reaches 3, the user loses.
 - Speaking Test button : to enter the speaking test page which contain the test picture, recording button, and answering button.
   when the user press recording button the system waits for the user's voice then converting it to text offline through vosk library.
   if the converted voice is correct, score increase by 1 else wrong answer's value increasing by 1.
   if wrong answer's value reaches 3, the user loses.
 - Leadboard page button : to enter scores page and show users names and scores.
