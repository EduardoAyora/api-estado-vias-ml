import tweepy
class IDPrinter(tweepy.StreamingClient):
    def on_tweet(self, tweet):
        print(tweet)

printer = IDPrinter("AAAAAAAAAAAAAAAAAAAAADC4igEAAAAAFN2leiur%2FgEX7T42zQB1HOsAnUc%3DgorTksh5Ij6BmO3Y7NLrZAPO3kFCr2DtGoopRqOQOGc3T3lGN0")
printer.add_rules(tweepy.StreamRule("@EduardoAyora64"))
# printer.delete_rules(["1620486800358744084"])
print(printer.get_rules())

printer.filter()