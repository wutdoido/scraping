# scraping
Self learning how to scrape websites for information

basic_scraper.py is a program that looks at the indeed page for Windsor jobs, sorting by date and pulls the Title, ensures it is located in Windsor, and creates a hyperlink for the job page.
Presently, simply outputs the data. 
Goal: Connect with local SQL to ensure that job listings are unique to their job link so I have a repository of jobs that I can sort depending on if i applied to them or not, and list the date at which the job was pulled. Also, want to make it automatic (likely just a shell script to run the program every 30 minutes)

Eventually, will expand this to LinkedIn page as well

