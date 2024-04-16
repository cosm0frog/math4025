# math4025
Study of Boston accent in audio corpora

There are a number of files associated with the analysis and visualization of this data for the project.
The three files [eɹ] formant difference gathering.py, [ɐɹ] formant difference gathering.py, and [ɑ] formant average gathering.py are the three notebooks used to analyze the raw data from Praat and Excel.

These files take the individual sheets from each excel book (which were extrapolated from the Praat phonetic data) and averages each sheet down to a single point of data by analyzing and averaging the different formant values over time, and then converts them into which ever variable we need.

The [ɑ] looks ends up with average F1 and F2 values, while the [eɹ] and [ɐɹ] gives us difference values, the difference between F2 and F1 and the difference between starting F3 and ending F3.

The files CapstoneModern_ar.py, CapstoneModern_er.py, CapstoneModern_o.py, CapstoneVisualization_ar.py, CapstoneVisualization_er.py, and CapstoneVisualization_o.py are the programs that produced the Python scatter plots when given the raw data in the form of pandas data frames.
