infile = open('trumptweets.txt', 'r', encoding='utf-8', errors='ignore')
fakenews_outfile = open('fakenews.txt', 'w')

# Counter
fake_news_counter = 0
retweet_counter = 0
source_iphone = 0
source_android = 0
source_other = 0

# Indexing
header = infile.readline().strip()
header_list = header.split('~')
text_index = header_list.index('text')
source_index = header_list.index('source')

# Counting Trump's tweets which mentioned 'Fake news'
for line in infile:
    fake_news_index = line.lower().find('fake news')
    if fake_news_index != -1:
        fakenews_outfile.write(line)

# Counting how many of those are retweets
        fake_news_counter += 1
        line = line.strip().split('~')
        if "RT @" in line[text_index]:
            ##adding '@' in the condition for skipping irrelevant "RT"s such as "Reporting", "party"...
            retweet_counter += 1

# Counting devices those tweets were sent
        if line[source_index].find("iPhone") != -1:
            source_iphone += 1
        if line[source_index].find("Android") != -1:
            source_android += 1
        if line[source_index].find("iPhone") == -1 and line[source_index].find("Android") == -1:
            source_other += 1

# Printer
print('There are', fake_news_counter, 'tweets that mentioned \'fake news\'.')
print('Within those tweets,', retweet_counter, 'of them are retweets.')
print('---\"Fake news\" tweets sources ---', '\n',
      'iPhone fake news tweets:', source_iphone, '\n',
      'Android fake news tweets:', source_android, '\n',
      'Other fake news tweets:', source_other)


infile.close()
fakenews_outfile.close()
