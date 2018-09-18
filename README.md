# ForensicsF-er
ForensicsF@%er is a script designed for Linux systems to demonstrate the unreliability of data-forensics by manipulating file timestamps on the EXT-4 filesystem.

# How It Works
In the simplest of explanations, ForensicsF@%er is designed to be triggered by an external event (e.g. a "dead-mans switch") where it will wait a user-defined time before manipulating files and updating the timestamps to the current one. The idea being that the date/time of the computer being taken into custody is well documented as part of standard operating procedure of the "Chain of Custody". As an anti-forensics tool it would (ideally) update prior to the imaging of a drive and change the file dates/times thus making the files appear to have been "planted" by a rogue policeman or investigator, discrediting not only the current investigation, but any other investigations prior and after and potentially leaving the investigator themselves liable for a litanny of criminal charges. The tool also self-purges after performing its' operations and deletes any/all system logs leaving no trace as to what has just occurred.

## How It Works (Extended)
The software does the following:
* Copies the selected file into a new inode
  * This is important because the C-Time is tied to when the inode was set, without hacking away at the Kernel it is impossible to set this manually, instead we simply copy the file to a new inode which updates the time for us.
* Shreds the old inode
  * This is also very important, it does us no good to copy and just delete, we have to also completely erase all the data in the old inode before we delete it. To do this, we rely on Linux's shred command, overwrite with null, and delete the file all in one go.
* Copies the new file to the old file
  * We change the file name of the copied file back to its' original name, not really important but it's good for asthetics.
* Shreds its own sourcefile, the list of files, and the logfiles
  * Obviously anti-forensic software is no good if the forensic investigator knows you are using it, so we need to clean up our act a little bit.
* Kills itself
  * Last bit of cleaning, we kill the process; I haven't worked in any special garbage collection or anything so the bits are going to remain in RAM for a while afterwards. Obviously this means that a dedicated forensic investigator can do a memory dump and see this program was run if they dump it early enough, however the actual file manipulation is run in subprocesses so the Kernel *should* automatically be freeing up that tasty, tasty RAM.

Note: This will break links because we haven't switched the inodes they're pointing to, it would be trivial to add support for this (e.g. by using find -inode and updating each symlink in the same manner). I left this feature out as this is just a proof of concept.

# Can I Use This To Do Something Illegal?
No. You are not authorized and I accept zero responsibility for any illicit uses of this software. It is for informational purposes only. I had planned on releasing this with a dead-man's switch, butit is not nearly as useful as most existing anti-forensics software out there. Not only that, but also the potential to damage innocent people's lives with charges of tampering, misconstruing, fabricating, or any of the littany of other offenses associated with not handling evidence appropriately along with the typical end-user of such products has swayed me against releasing the full program. If you aren't able to figure it out yourself, you really should not be doing anything even remotely illegal using a computer anyway.

# Why Did You Make This?
Partially for the fun of it, but also to point out that computer forensic evidence is flawed. It may take hours from the time a laptop is seized until the time the disk drive is imagedl during that time the laptop will go from a "beat" police officer to another to a detective who will retrieve it from the evidence room, likely open it up to see if he can get in before calling a forensics investigator which could take days to weeks depending on how important the case is. That is a very, very long time for a computer to be sitting, and we can't rely on evidence that has the potential to delete or change itself. Not only that, but an individual could use a program similar to this one to make it appear as if a file is OLDER than it really is by modifying it to change the system date/time and thereby use it to fabricate evidence.

In short, I made it because Computer Forensics is flawed in this regard, the flaw needed to be pointed out, and because I had a couple hours to kill.

# How To Use:
It's pretty simple, just type `python3 forensicfucker.py` into a terminal then check the results in SmokingGunTimes you will see the file times have changed. To view the creation time is a bit more difficult as stat does not yet fully support the "birth" or "creation" time. In order to view the creation time, use `debugfs -R 'stat <inode_number>' DEVICE` [click here for a more detailed explanation](https://unix.stackexchange.com/questions/50177/birth-is-empty-on-ext4/50184#50184)

# Why isn't it self-destructing?
It's set to not self-destruct by default, if you open up the .py file and change the setting `self_destruct = False` to `self_destruct = True` it will automagically erase the python script, the the SmokingGunTimes file, the list of files, and the system logfiles then it will kill itself ending the process. Must be run as root to delete the logfiles, you can comment out the line that says `delFile("/var/logs")` if you want to run it as a standard user and without deleting the logfiles.
