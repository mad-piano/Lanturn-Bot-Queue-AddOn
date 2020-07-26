# Lanturn-Bot-Queue-AddOn
This is additional code that will add features that the Original Lanturn bot intended, but never implemented.
You may have realized that Lanturn bot's "print queue", never worked. This code will help fix that issue.

**You need to edit certain placeholders in the code, it is pointed out in the code**

>What's new/different than the previous Lanturn bot?
* Added new commands
* Additional working queue

>New Commands List
* $List - The bot will send the entire queue in a neat, and numbered embed list.
* $MyPlace - The bot will tell the invoker what position they are in the queue.
* $QueueSize - The bot will send the size of the queue.

>How do I implement this code to my Lanturn bot?
*Replace the on_message event in the bot.py file in Lanturn bot, and add the one I created.
*Add the lists in the same file by the imports; add the commands somewhere appropriate in the RaidCommands file.

