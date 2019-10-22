## Menu
* greet
  - utter_greet
* read_menu
  - action_show_menu
* goodbye  
  - utter_goodbye
  - action_restart

## Pizza
* greet
  - utter_greet
* order_pizza{"pizza_name": "margherita"}
  - action_confirm_pizza
  - action_restart

## Only Pizza
* order_pizza{"pizza_name": "ortolana"}
  - action_confirm_pizza
  - action_restart
