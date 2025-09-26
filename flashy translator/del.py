from PIL import Image
import pandas

fr_file=pandas.read_csv("data/french_words.csv")
fr_dict=fr_file.to_dict(orient='records')       #orient records will rearrange the dict [{'French': 'partie', 'English': 'part'}, {'French': 'histoire', 'English': 'history'},...] in this format so it makes it easy to tap into values.
fr_csv=fr_file.to_csv(index=0) 

fr_dict.remove({'French': 'partie', 'English': 'part'})
print(fr_dict)