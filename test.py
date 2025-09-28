import snscrape.modules.twitter as sntwitter
import pandas as pd

query = "xeet.ai"  # or "https://xeet.ai/boost" for stricter match
max_results = 500  # Or however many you want

results = []

for i, tweet in enumerate(sntwitter.TwitterSearchScraper(query).get_items()):
    if i >= max_results:
        break
    results.append({
        "username": tweet.user.username,.0
        .00.
        "display_name": tweet.user.displayname,
        "tweet": tweet.content,
        "date": tweet.date,
        "url": tweet.url
    })

df = pd.DataFrame(results)
df.to_csv("xeet_tweeters.csv", index=False)
print("✅ Saved", len(df), "results to xeet_tweeters.csv")
