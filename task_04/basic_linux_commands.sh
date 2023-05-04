#!/bin/bash

# Task 1: Create a new user account named "johndoe" with a password "password123".
useradd -m johndoe -p "password123"

# Task 2: Assign the user account "johndoe" to the group "developers".
usermod -a -G developers johndoe

# Task 3: Verify that the user account "johndoe" has been created and is a member of the group "developers".
grep johndoe /etc/passwd
groups johndoe

# Task 4: Change the permissions of a file named "file.txt" to allow the owner to read, write, and execute, and allow the group and other users to only read.
chmod 744 file.txt

# Task 5: Create a folder name “backup” and copy a file named "file1.txt" to a directory named "backup".
mkdir backup
cp file1.txt backup/
