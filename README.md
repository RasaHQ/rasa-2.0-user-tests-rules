# User Interview

## Resources

* [Rasa Open Source 2.0 Documentation](https://rasa.com/docs/rasa/next)

## Task 1: Create FAQ

In case the user sends a message with the intent `bot_challenge` , the assistant should
always reply with `I am a bot, powered by Rasa.` Please add the necessary rule.

## Task 2: Add a conditional rule

Please change the rule from Task 1 so that it only applies when the slot `is_a_bot`
was set to `True`.

## Task 3: Create a Form

Please define a form which asks the user for feedback and stores it in the slot
`feedback`. Once the user provided the feedback, the assistant should thank the user
for providing the feedback.

## Task 4: Create a Fallback

NLU messages are often classified with low confidence levels. Please write a rule
which asks the user to rephrase whenever a received message receives a lower
confidence than 0.5.
