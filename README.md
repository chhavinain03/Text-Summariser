---
license: unlicense
---

# Text Summarizer

This Project provides you with a brief summary of the given Text.
The Project allows you to paste or Upload PDF file to summarize it , It also allows you to customize the summarization % of the Final summary!

## Concept
The Project is based on the concept of Extractive Text Summarization.
In this concept we read all the sentences given in the TEXT and then spereate each word in them. 
Then we grade each of the unique words with a value which corelates to the number of times it has occured in the text.

Then we normalize these grades and reassign them to all the words in the sentences. Then we calculate the grades for the whole sentences and rank the sentences on the grades they get.
Then we summarize the top "n%" of the sentences as output.
<img src='https://imgs.search.brave.com/m5dNQYnKvcBHxQBBwzS_lUNmEKAEMcA3WvZZ9EYvQSM/rs:fit:1200:1016:1/g:ce/aHR0cHM6Ly9taXJv/Lm1lZGl1bS5jb20v/bWF4LzI5MjAvMSo1/X3Q0RUpsMUl5OUIx/dzVFdFgxWm9nLmpw/ZWc'>
## Deployment

The Project is Deployed on Hugging face 

```bash



 
