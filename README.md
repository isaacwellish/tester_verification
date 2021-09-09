# tester_verification
for automating the tester verification process

1. Clone / download project and save in a known location
2. Open WO email once the ordered list from Andy/whomever is sent
3. Copy text from email
4. Open terminal and go to folder at the above location ^^
5. touch NAMEOFWODAYFILE (creates the file)
6. vim NAMEOFWODAYFILE (opens in vim editor)
7. Paste text into VIM (type 'i' to insert then paste)
8. esc, save and close (esc, :wq, enter)
9. Run this command: python3 verify_sort.py NAMEOFWODAYFILE
10. Program will output the raw list of WOs with the full PIDs and SKUs (to compare with #12 below)
11. Then will print just the WO#s
12. Voila

![alt text](https://github.com/isaacwellish/tester_verification/blob/master/output.png?raw=true)

