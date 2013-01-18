#!/usr/bin/env python
# coding: utf-8

import glob
import os

import eyed3
import baker


def set_id3(file_path):
    '''
    Function takes path to mp3 file for setting id3 tags by file name.
    '''
    if not os.path.isfile(file_path) or not file_path.endswith('.mp3'):
        return

    audio = eyed3.load(file_path)
    fname, extension = os.path.splitext(file_path)

    artist, title = fname.replace('\xe2\x80\x93', '-').split('-')
    artist = artist.strip().capitalize().decode('utf8')
    title = title.strip().capitalize().decode('utf8')

    audio.tag.artist = artist
    audio.tag.title = title
    audio.tag.save()


@baker.command(shortopts={"dirname": "d"})
def set(dirname=None, *files):
    '''
    Function takes mp3 files or directory with mp3 files
    and set id3 tags (Artist, Title) by file name.

    :dirname: Direcgtory with mp3 files.
    :files: List of mp3 files.
    '''
    if dirname:
        files = glob.glob(os.path.join(dirname, '*.mp3'))

    for fname in files:
        print 'Changing %s id3 tags.' % fname
        set_id3(fname)

baker.run()
