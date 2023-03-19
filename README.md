# ArgPoll
JOUR 628O Bot Project: Argentina 2023 election polls bot

Update 3/19/2023:

Objective: Create a bot that scrapes the HTML table under "By political party, 2023" and gives new updates weekly about new polls.
URL: https://en.wikipedia.org/wiki/Opinion_polling_for_the_2023_Argentine_general_election

Scraping has proven to be very difficult, so much so I've had to ask Chat GPT for help in creating a code that deals with all the nuances and problems that are going on with that particular HTML table. For starters. I wanted to use the table from the Spanish wikipedia version of that page (https://es.wikipedia.org/wiki/Anexo:Encuestas_de_intenci%C3%B3n_de_voto_para_las_elecciones_presidenciales_de_Argentina_de_2023), but after going through difficulties, I learned that the formatting of the spanish page is not suited to be scraped, for whatever reason. I asked ChatGPT to look at that URL and it said the "Por partido político
2023" table was not an HTML table but a large image, not able to be scrapped, so back to the english site I went.

Scraping the English table proved hard. At first things were ok, but I had to continually specify which table I wanted. After that, the headings were simply not coming up beause the headings for that table are images / logos that link to the political party's wiki page. Finally, I had to make sure that the headings for the non-political party elements, such as date and polling firm, were in the right places.
It basically took hours of trial and error asking chart GPT to keep regenerating codes with small revisions to take into account all the nuances of the table. I can't show you EVERYTHING I asked, because it was a lot, but I can give you an idea:

When I initially asked to generate a code, I asked it:

"Hey can you look at this URL For me?
"Ok, do you see that table there under "By political party 2023"?
"Can you write a python code that scrapes from that table into a CSV?"

Getting that code was the easy part, going through constant revisions was the hard part. Here is what I asked in the last chat:

Me: Hey can you take a look at this python code for me?
AI: Of course! I'd be happy to take a look at your Python code. Please provide the code and any additional context or instructions that you have, and I'll do my best to help you out.
Me: *inserts code*
AI: This code appears to be scraping data from a Wikipedia page about opinion polling for the 2023 Argentine general election and writing it to a CSV file.
Me: So there is a problem with the headings. They're there but they're not in the right place. However, when I try to modify the code, it won't work or when the headings are fixed, the data completely disappears and it only leaves the row with the headings. Can you help me?
AI: Sure, I can help you with that!

It's possible that the code is not extracting the table headers correctly. One way to fix this is to find the index of the "Pollster" column and move it to the front of the headers list.

Here's a modified version of the code that should fix the issue: *Insersts code into convo*
Me: Ok, just replace "pollster" with polling firm
AI: Sure, I can modify the code to use "polling firm" instead of "pollster" as the column name.

Here's the modified code: *Inserts code*
ME: cool, another thing, so the other headings are in the right places, but "polling firm" is where the date should be, can you switch those two?
AI: Sure! To switch the "Polling firm" column header with the "Date" column header, you can modify the code to replace the respective headers in the headers list.

Here's the updated code: *inserts code*
Me: can you replace date with "Fieldwork date"
AI: Sure! To replace the "Date" column header with "Fieldwork date", you can modify the code to replace the respective header in the headers list.

Here's the updated code: *inserts code*
ME: This came up: Traceback (most recent call last):
  File "/workspaces/ArgPoll/scraper/wikitable/scrape.py", line 22, in <module>
    date_index = headers.index("Date")
ValueError: 'Date' is not in list
AI: I'm sorry to hear that. It seems that the script is trying to find the index of the "Date" column in the headers list, but it can't find it. This might be because the column header has been modified or is missing from the table.

To fix this error, you can try adding a print statement to see the headers list and confirm whether "Date" is present in it or not. For example, you can add the following line of code before the date_index variable is assigned:*Inserts code*


Basically this went on and on for hours. I would get new code, put it into my scrape.py, run it, check the CSV, and then go back and ask the AI to make modifications to make it better.

In the end I was able to get the code that is in the scrape.py file and it STILL is not perfect. The headings and most rows are ok, but one polling entry is not. Its "Opinia Argentina" from February 18-27. They had two sets of polls for the same day. The code puts the second set of data in the wrong cells, but it doesn't completely mess up the table. Eventually I just called it a day on that issue and I will continue on it later.

Where I go from here: The next steps of this is to program this webscraper to periodically run. I will set the intervals to once a week since that seems to be the cycle of release of opinion pollings in Argentina related to the election. 

After that I need to transfer that into an email bot which I am not sure how to do yet but I will deal with that at a later time.

What blockers have I recieved? The wonky HTML table I am parsing from. It has A LOT of problems. The headings were off, polls with two sets of data are wonky, I might need to ask Simon for help with this. Next step though will be the timed scraping so we will see if that encounters any problems.

When I spoke to you in class about creating the code, I want you to know I scrapped that code because the CSV file it was creating was VERY messy and had outdated information. 

What have I learned? Scraping is MESY BUSINESS. I apologize for relying heavily on ChatGPT for this assignment, but I will say the explanations it gave me for the problems in the codes were wayyy over my head that, without it, I probably would be spending much more time than I did just creating the web scraper. Work smarter not harder I guess. 

Whats the best version? I ultimately want a bot with a clean CSV file, no errors, and gives me updated information. The best version could be one that scrapes the individual candidates, but since the primaries for the Argentine presidential election aren't until August, that is redundant right now.... somewhat I guess? You still could. I do remember asking Chat GPT if, in the URL: https://en.wikipedia.org/wiki/Opinion_polling_for_the_2023_Argentine_general_election
I asked if the table: "By candidate Before candidates definition" if this table is a good table to scrape and it said something like : "No its not, its very complex and would require a very unique code to scrape." I'll ask it again later. 


