# Text Analysis Project - Drake vs. Taylor Swift

## Overview

For this project I used Python to compare the language used on the Wikipedia pages for Drake ans Taylor Swift who are both musicians in different generes. The goal was to:

1. Programmatically download text from the internet (I used Wikipedia to get all the info needed)
2. Clean and process the text
    a. Wanted to remove common stopwords 
    b. Analyze the word frequencies 
    c. Visualize the most common words
3. Try an advanced text techinque #AI helped with this part 

This satisfies the project requirements for text harvesting, cleaning, analysis, visualization, and at least one optional extension.


## Implementation & Data Collection

I used `wikipedia-api` library to download the plain-text content of two pages:

- `"Drake (musician)"`
- `"Taylor Swift"`

This is handled in the function:
- `fetch_wikipedia_text(title)` --> creates a `Wikipedia`object with a `user_agent` and return `page.text` for all the given song titles.

## Text cleaning and processing

I wrote several functions to transform the raw article text into something I could look at: 
 -`clean_text`
 - lowercases for all the text
 - remove any punctuation using `string.punctuation`
 - remove any numbers or digits 
 - spilts the text into a list of words

- `remove_stopwords(words)`
- filter out workds like "the", "and", "is", "it", and many more

## Word frequency and stats needed

 `word_frequencies(words)`  
  - Builds a dictionary mapping each word to how many times it appears.

- `summary_stats(words)`  
  - Computes:
    - total word count  
    - number of unique words  
    - average word length  

These functions are applied separately to Drake’s and Taylor Swift’s pages after cleaning and stopword removal.

## Advanced Technique – Text Similarity (Cosine Similarity)

As my optional advanced technique, I calculated the **cosine similarity** between the word-frequency dictionaries for Drake and Taylor Swift.

My result was **0.3873**, which shows that Drake and Taylor Swift’s Wikipedia pages share some similar language (like “music” and “album”) but still have noticeable differences in focus.  

- Drake’s page focuses more on albums, chart rankings, and rap music.  
- Taylor Swift’s page emphasizes country/pop genres, awards, and tours.

### Use of AI

Parts of this project (especially the structure of helper functions and some boilerplate code) were developed with assistance from ChatGPT. I integrated the code into my own project, ran and debugged it, and decided which features and comparisons to include. When I did get errors when trying to pull the data, I asked AI to help me understand what was wrong and fixed it. 


## RESULTS 

Summary stats: 

Drake:
- total words: 7555
- unique words: 2757
- avg length: 6.27

Taylor Swift: 
- total words: 5773
- unique words: 2310
- avg length: 6.48

Top 15 words for Drake: 
drake : 281
album : 66
music : 64
released : 63
drakes : 57
one : 50
billboard : 49
songs : 47
later : 40
first : 39
most : 39
number : 37
artist : 36
hot : 35
song : 35


Top 15 words for Taylor Swift: 
swift : 156
music : 70
country : 68
album : 60
first : 49
swifts : 45
billboard : 41
pop : 40
year : 39
awards : 39
artist : 37
one : 37
albums : 35
tour : 33
top : 28

ASCII bar chart for Drake:

          drake | ######################################## (281)
          album | ######### (66)
          music | ######### (64)
       released | ######## (63)
         drakes | ######## (57)
            one | ####### (50)
      billboard | ###### (49)
          songs | ###### (47)
          later | ##### (40)
          first | ##### (39)
           most | ##### (39)
         number | ##### (37)
         artist | ##### (36)
            hot | #### (35)
           song | #### (35)

ASCII bar chart for Taylor Swift:

          swift | ######################################## (156)
          music | ################# (70)
        country | ################# (68)
          album | ############### (60)
          first | ############ (49)
         swifts | ########### (45)
      billboard | ########## (41)
            pop | ########## (40)
           year | ########## (39)
         awards | ########## (39)
         artist | ######### (37)
            one | ######### (37)
         albums | ######## (35)
           tour | ######## (33)
            top | ####### (28)



## Reflection 
This project taught me how to take a real piece of text from the internet and turn it into structured, analyzable data using Python.

Some main steps that I learned were: 
- working with APIs and pulling info from an internet source
- text cleaning and removing repeats 
- using discint words for counting 
- how to make the bar chart to show the difference between both musicians 

If I would to contuine this project, I would compare actual song lyrics and try doing a similar functions between the two. I would like to see what words are the most repeated in songs. 

# Final Thoughts 
Overall this assignment helped me strength my skills by using different APIs and texts. It was extremely nice to see when my code went through without any errors. 