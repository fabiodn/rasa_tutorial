# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


#This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

menu = ''
with open('data/pizze.txt', 'r') as f:
    menu = f.read()
print(menu)


class ActionShowMenu(Action):

    def name(self) -> Text:
        return "action_show_menu"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(menu)
        return []

class ActionConfirmOrder(Action):

    def name(self) -> Text:
        return "action_confirm_pizza"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        pizza_name = tracker.get_slot('pizza_name')

        if pizza_name is None:
            dispatcher.utter_message(f'Non ho capito la tua pizza me la puoi ripetere?')
        elif self.is_on_menu(pizza_name):
            dispatcher.utter_message(f'L\'ordine della sua pizza {pizza_name} è stato preso in carico!')
        else:
            dispatcher.utter_message(f'La pizza {pizza_name} non è sul nostro menù, ci scusiamo per il disagio') 
        return []
    
    def is_on_menu(self, pizza_name :str):
        return f'{pizza_name.capitalize()}' in menu



