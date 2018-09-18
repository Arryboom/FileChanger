# ForensicsF-er
ForensicsF@%er is a script designed for Linux systems to demonstrate the unreliability of data-forensics by manipulating file timestamps on the EXT-4 filesystem.

# How It Works
In the simplest of explanations, ForensicsF@%er is designed to be triggered by an external event (e.g. a "dead-mans switch") where it will wait a user-defined time before manipulating files and updating the timestamps to the current one. The idea being that the date/time of the computer being taken into custody is well documented as part of standard operating procedure of the "Chain of Custody". As an anti-forensics tool it would (ideally) update prior to the imaging of a drive and change the file dates/times thus making the files appear to have been "planted" by a rogue policeman or investigator, discrediting not only the current investigation, but any other investigations prior and after and potentially leaving the investigator themselves liable for a litanny of criminal charges. The tool also self-purges after performing its' operations and deletes any/all system logs leaving no trace as to what has just occurred.

# Can I Use This To Do Something Illegal?
No. I planned on releasing this with a dead-man's switch, but if I did that I might as well have written a script to wipe the drive instead as that would be much safer than hoping a court didn't see through your tricks. Not only that, but the potential to damage innocent people's lives with charges of tampering, misconstruing, fabricating, or any of the littany of other offenses associated with not handling evidence appropriately.

# Why Did You Make This?
Partially for the fun of it, but also to point out that computer forensic evidence is flawed. It may take hours from the time a laptop is seized until the time the disk drive is imagedl during that time the laptop will go from a "beat" police officer to another to a detective who will retrieve it from the evidence room, likely open it up to see if he can get in before calling a forensics investigator which could take days to weeks depending on how important the case is. That is a very, very long time for a computer to be sitting, and we can't rely on evidence that has the potential to delete or change itself. Not only that, but an individual could use a program similar to this one to make it appear as if a file is OLDER than it really is by modifying it to change the system date/time and thereby use it to fabricate evidence.

In short, I made it because Computer Forensics is flawed in this regard and it needed to be pointed out.

# How To Use:
It's pretty simple, just type
    python3 forensicfucker.py
into a terminal then check the results in SmokingGunTimes

# Why isn't it self-destructing?
It's set to not self-destruct by default, if you open up the .py file and change the setting "self_destruct = True" it will automagically erase the python script, the the SmokingGunTimes file, and the list of files then it will kill itself ending the process. 
