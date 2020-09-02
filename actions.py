from rasa_sdk.interfaces import Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction

from typing import Text, List, Dict, Union, Any


class FeedbackForm(FormAction):
    def name(self) -> Text:
        return "feedback_form"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        return ["feedback"]

    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        return {
            "feedback": self.from_text()
        }

    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:
        """Define what the form has to do
            after all required slots are filled"""

        # utter submit template
        dispatcher.utter_message(template="utter_thanks_for_feedback")
        return []