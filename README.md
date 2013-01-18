Set id3 tags by file name
===================

This is a small script for setting "Artist" and "Title" mp3 id3 tags by file name.

Requirements
====================
 - Baker==1.3
 - eyeD3==0.7.1

Usage:
====================
Find all mp3 files in directory **dirname** and set id3 tags by their file names:

    id3.py set -d dirname


Get files **artist1–title1.mp3** and **artist2–title2.mp3** and set id3 tags by their file names:

    id3.py set artist1–title1.mp3 artist2–title2.mp3
