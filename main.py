import openai
import requests
from bs4 import BeautifulSoup
import csv


# Set the API key
openai.api_key = "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"

# Choose the model
def openaiChat(question):
    model_engine = "text-davinci-003"

    # Generate text
    prompt = question
    completion = openai.Completion.create(engine=model_engine, prompt=prompt, max_tokens=1024, n=1,stop=None,temperature=0.5)
    message = completion.choices[0].text
    return message




#pull data from website
def single_webpage_scraper(URL):
    num_chars = 3_000
    all_text_homepage = ""
    res = requests.get(URL)
    soup = BeautifulSoup(res.content, "html.parser")
    tag = soup.body
    for string in tag.strings:
        all_text_homepage += string

    return all_text_homepage[:num_chars]



#company = single_webpage_scraper("https://www.convertflow.com/").strip()
#print()

def cover_letter(company, description, jobTitle, name):
    prompt = "take my resume:"
    resume = open("Drew_resume.txt", "r").read()
    prompt += resume
    prompt += "and write a cover letter  for "+ name +"applying for the position as" + jobTitle + " at " + company + "based on these qualifications:"
    prompt += description
    return openaiChat(prompt)

csv_file = open("Get a job.csv", "r")
csv_reader = csv.reader(csv_file)
next(csv_reader)
for line in csv_reader:
    company = line[0]
    description = line[1]
    jobTitle = line[2]
    print(cover_letter(company, description, jobTitle, "Drew"))
