import random
import datetime

reminders = {}

def get_response(message: str) -> str:
    p_message = message.lower()

    if p_message == '!mavgreeting':
        return "`hey there!`"

    if p_message.startswith('!mavsetreminder'): #!mavsetreminder 2024-01-03 15:30:00 Attend Meeting ex
        # Extracting time and message from the command
        _, date_str, time_str, reminder_message = p_message.split(maxsplit=3)

        try:
            # Parsing date and time and converting them to a datetime object
            reminder_time = datetime.datetime.strptime(f"{date_str} {time_str}", '%Y-%m-%d %H:%M:%S')

            # Adding reminder to the dictionary
            reminders[reminder_time] = reminder_message

            return f"`Reminder set for {date_str} {time_str}: {reminder_message}`"
        except ValueError:
            return "`Invalid date or time format. Please use 'YYYY-MM-DD HH:MM:SS'.`"

    if p_message.startswith('!mavdelreminder'): #!mavdelreminder 2024-01-03 15:30:00 ex
        # Extracting date and time from the command
        _, date_str, time_str = p_message.split(maxsplit=2)

        try:
            # Parsing date and time and converting them to a datetime object
            reminder_time = datetime.datetime.strptime(f"{date_str} {time_str}", '%Y-%m-%d %H:%M:%S')

            # Removing reminder if it exists
            if reminder_time in reminders:
                del reminders[reminder_time]
                return f"`Reminder deleted for {date_str} {time_str}`"
            else:
                return f"`No reminder found for {date_str} {time_str}`"
        except ValueError:
            return "`Invalid date or time format. Please use 'YYYY-MM-DD HH:MM:SS'.`"


    if p_message == '!mavviewreminder':
        if not reminders:
            return "`No reminders set.`"

        # Formatting reminders for display
        reminder_list = [f"`{time}: {message}`" for time, message in reminders.items()]
        return "`Reminders:\n`" + "\n".join(reminder_list)


    if p_message == '!mavcoinflip':
        if random.randint(1, 2) == 1:
            return "`heads`"
        else:
            return "`tails`"

    if p_message == '!mavroll':
        return str(random.randint(1, 6))

    if p_message == '!mavhelp':
        return("`Here is a list of commands you can use! \n !mavgreeting - Lets Mav greet the user. \n !mavsetreminder - Lets the user set a new reminder: Set a reminder. Usage example: !mavsetreminder 2024-01-03 15:30:00 Attend Meeting \n !mavviewreminder - Lets the user view all the reminders. \n !mavdelreminder - Lets the user delete a reminder. Usage Example: !mavdelreminder 2024-01-03 15:30:00 \n !mavcoinflip - Lets Mav do a coin flip resulting in heads or tails. \n !mavroll - Lets Mav roll a dice.`")









