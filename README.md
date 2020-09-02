# User Interview

## Resources

* [Rasa Open Source 2.0 Documentation](https://rasa.com/docs/rasa/next)

## Task 1: Migrating FAQs

The provided assistant has currently twho FAQs which are implemented using the
`MappingPolicy`. Please replace the intent mappings which adequate rules which
implement the same behavior.

## Task 2: Create FAQ

In case the user sends a message with the intent `bot_challenge` , the assistant should
always reply with `I am a bot, powered by Rasa.` Please add the necessary rule.

## Task 3: Migrating a Form

Our provided assistant defines a `feedback_form` in the old Rasa Open Source 1 format
within `actions.py`. Please migrate this form to Rasa Open Source 2.

## Task 4: Migrating Fallbacks

Our provided assistant defines a fallback policy in its model configuration 
`config.yml`. Please migrate the fallback handling from the `FallbackPolicy` to its 
Rasa Open Source 2 counterpart.
