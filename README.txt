README.txt File for Loehr-Salazar Lab 8 Submission

-The data for the hash baseline is stored in /tmp/hashBaseline.csv
-There are three columns in the csv file--> FILENAME (FULL PATH), HASH, and DATE-TIME
-Each row represents a singular entry for a file with the filename, hash, and date-time in the corresponding
 columns as explained above. 
 
-After a hash comparison is complete, any modifications to files that were detected are written to /tmp/modifications.txt
-A sample format for an entry in the modification file is provided below:
        FILNAME (FULL PATH)
        -------------------
        /var/cache/samba/browse.dat
        SHA256 HASH                                                            DATE-TIME
        -----------                                                            ---------
        79703ce882bf5006b3bfaa2ba588d45d8ded853bb4f0be88a888e1aed6ef249f       2021-03-29T23:42:07.305394