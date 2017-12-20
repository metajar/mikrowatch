## Mikrowatch
---
Simple script used to monitor for new devices on your LAN. Nothing fancy and 
leverages RouterOS's APIs to look at ARPs and compare them to known. This was
written in around 30 minutes so it is nothing too fancy but can be used for a 
quick way to watch for new devices. 

You will want to install all the requirements for requirements.txt and setup a cronjob to run 
the script every minute.