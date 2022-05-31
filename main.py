from insta_follower import InstaFollower, FANPAGE_NAME

bot = InstaFollower()
bot.login()
bot.find_followers(FANPAGE_NAME)

#bot.find_followers(INPUT_ANOTHER_FANPAGE)

