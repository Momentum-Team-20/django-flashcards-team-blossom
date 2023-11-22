# Team Blossom Flashcards

# Project Description

Our flashcard project opens to a Home page where user registers and logs in.
User can create a new deck of flashcards. Their user-specific home page shows a list of all decks, with links to "play" (which is to start a page where a flashcard is shown and the 'game' begins) and create new flashcards. User can add new flashcards with a question and an answer. User can move through deck one card at a time and click "next card" to see a new card. User can select if they got the question right or wrong.

# Kelsey

Skills Practice:

- Navigating while others coded, researching code to try out from Google researches
- Communicating as clearly as possible through Slack, git commit notes, and generally working with code in a far more collaborative nature
- Trial and error with hands on writing code
- adding Javascript files to Django environment
- iTerm commands like pipenv install, git pull, virtual environments, etc.

Key Takeaways:

- One change to code must be reflected across all the files. All the urls, the views, the templates, all have to be in connection for something to work properly. To know Django is to know how these files speak to each other.
- Sometimes it's OK to be really pedantic about how you're processing information and what you call it in your code. The models really are something you should consider because choices really become apparent later down the line.
- The error pages are always pointing you to where you should be looking; it's meant to help you if you can interpret it or find someone who can.

Challenges:

- The code for this often felt deceptively simple, take something like "pk=pk": It takes much longer to explain it in context of your code than to actually write it. Complicated code can be very just a few lines. This project is full of code that does a lot with very little text, and it can be very hard to keep track of all of the minor keywords or terms. My biggest challenge was understanding the primary keys, ids, etc. and how to pull that information and when to.

# Freddie

Skills Practiced:

- Writing views, urls, and templates
- writing models and forms
- debugging in the shell
- Adding javaScript and CSS to the django project

Key Takeaways:

- Giving the url in the template all the correct info it needs for the view to render properly (ie deck.pk)
- This project really solidified for me the relationship of templates, views, and urls.
- Using QuerySets to pull objects out of the database

Challenges:

- There are a lot of pieces that go into the whole thing really, but particularly into views that has been challenging to keep up with. Breaking things down as much as possible helps to know what to pass to the view and write in the view context.

# Roadmap

- Saving data for correct/incorrect answers so that a correct card does not reappear in the deck and an incorrect card will appear again
- Restart the deck to include all cards
- Be able to search decks
- User could share decks with another specific user to study together
- User can organize decks according to subject, alphabetically, etc.
- Styling
  - centering text inside flash cards
  - arranging flashcard on viewpage
  - a celebration after user correctly answers all the cards (confetti or fun gif)
