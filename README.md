Some scripts to read and show a sequence profile in browser.

Main components:
- sequence_profile_io.py
      Reads .profile file and prints tuple with three elements: ([amino acids'
      symbols], [amino acids], [reversed matrix]).
      usage: sequence_profile_io.py [-h] -f FILE

- draw_sequence_profile.py
      Draws and saves a sequence profile as .svg file.

- show_sequence_profile.html
      Displays a user's sequence profile in browser.


What is necessary to use it?
- visualife ('https://visualife.readthedocs.io/')
- brython ('https://brython.info/')
