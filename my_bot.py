import random
from secret import my_username
from pick_number import pick_number
from datetime import date, time, datetime

"""
**Do NOT change the name of this function.**

This function will be called every time anyone says anything on a channel where the bot lives.

* It returns `True` if the bot notices something it wants to repond to.
* You can have certain words or patterns in the messages trigger the bot.
* You can have the bot respond differently to different users
"""
def should_i_respond(user_message, user_name):
  if user_message == "What's your name?":
    return True
  elif user_message == "Say pi":
    return True
  elif "Pick a number" in user_message:
    return True
  elif user_message == "What's the time?":
    return True
  elif user_message == "What's the date?":
    return True
  elif "How far away is" in user_message:
    return True
  elif user_message == "Flip a coin":
    return True
  elif user_message == "How old are you?":
    return True
  elif user_message == "What is the purpose of life?":
    return True
  elif user_message == "achoo":
    return True
  else:
    return False

"""
**Do NOT change the name of this function.**

This function will be called every time the `should_i_respond` function returns `True`.

* This function returns a string.
* The bot will post the returned string on the channel where the original message was sent.
* You can have the bot respond differently to different messages and users
"""
def respond(user_message, user_name):
  if user_message == "What's your name?":
    return "My name is botboy!"
  elif user_message == "Say pi":
    return "3.141592653589793238462643383279 ... I forgot the rest... sorry"
  elif "Pick a number" in user_message: ############
    numbers = "0123456789"
    i = 1
    for letter in user_message:
      if user_message[-i] in numbers:
        i = i + 1
      else:
        break
    Upper_Limit = user_message[(-i + 1):]
    for letter in user_message:
      if user_message[-(i + 5)] in numbers:
        i = i + 1
      else:
        break
    Lower_Limit = user_message[(-i + 1):-(i + 4)]
    random_number = pick_number(Lower_Limit, Upper_Limit)
    return f"A random number between {Lower_Limit} and {Upper_Limit} is {random_number}"
  elif user_message == "What's the time?":
    current_date = datetime.now()
    return f"the time is {current_date.time()}"
  elif user_message == "What's the date?":
    return f"the date is {date.today()}"
  elif "How far away is" in user_message:
    year = user_message[16:20]
    month = user_message[21:23]
    day = user_message[24:26]
    questioned_date = datetime(int(year), int(month), int(day))
    date_now = datetime.now()
    distance = questioned_date - date_now
    if distance.days == "1":
      return f"It is {distance.days} day away"
    else:
      return f"It is {distance.days} days away"
  elif user_message == "Flip a coin":
    side = random.randint(1, 6000)
    if side == 6000:
      coin_side = "on its side"
    elif side % 2 == 0:
      coin_side = "tails"
    elif side % 2 == 1:
      coin_side = "heads"
    return f"the coin is {coin_side}"
  elif user_message == "How old are you?":
      birth = datetime(2026, 1, 1)
      date_now = datetime.now()
      days_old = date_now - birth
      if days_old.days == "1":
        return f"I'm {days_old.days} day old!"
      else:
        return f"I'm {days_old.days} days old!"
  elif user_message == "What is the purpose of life?":
    return "Error 404"
  elif user_message == "achoo":
    return "bless you"