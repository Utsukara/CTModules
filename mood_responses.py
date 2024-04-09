happy_moods = ['happy', 'joyful', 'excited', 'content', 'peaceful', 'loving', 'hopeful', 'grateful', 'optimistic', 'proud', 'confident', 'inspired', 'amused', 'ecstatic', 'elated', 'enthusiastic', 'euphoric', 'exhilarated', 'exuberant', 'gleeful', 'jubilant', 'lighthearted', 'merry', 'overjoyed', 'radiant', 'thrilled', 'upbeat', 'vibrant', 'victorious', 'zestful', 'zesty', 'zippy', 'zappy', 'zany']
sad_moods = ['sad', 'depressed', 'gloomy', 'mournful', 'somber', 'sorrowful', 'tearful', 'unhappy', 'upset', 'down', 'blue', 'downcast', 'downhearted', 'downhearted', 'down in the dumps', 'down in the mouth', 'low', 'low-spirited', 'melancholy', 'miserable', 'woeful', 'wretched', 'despondent', 'disconsolate', 'distressed', 'doleful', 'forlorn', 'glum', 'heartbroken', 'heartsick', 'heavyhearted', 'joyless', 'lachrymose', 'lugubrious', 'morose', 'woebegone', 'down in the mouth', 'down in the dumps', 'downhearted', 'downcast', 'disheartened', 'dispirited', 'discouraged', 'dejected', 'despondent', 'crestfallen', 'choked up']
angry_moods = ['angry', 'mad', 'enraged', 'furious', 'indignant', 'irate', 'livid', 'outraged', 'resentful', 'sullen', 'bitter', 'cross', 'displeased', 'exasperated', 'fuming', 'incensed', 'infuriated', 'irritated', 'offended', 'provoked', 'riled', 'sore', 'upset', 'vexed', 'wrathful', 'aggravated', 'annoyed', 'choleric', 'disgruntled', 'disgusted', 'frustrated', 'impatient', 'irascible', 'irksome', 'irritable', 'peevish', 'petulant', 'testy', 'tetchy', 'touchy', 'unhappy', 'unpleasant', 'unpleased', 'unquiet', 'uptight', 'waspish', 'wroth', 'wrathful', 'wrathy']

def mood_responses(mood):
    if mood in happy_moods:
        return "I'm glad to hear that you're feeling " + mood + "!"
    elif mood in sad_moods:
        return "I'm sorry to hear that you're feeling " + mood + "."
    elif mood in angry_moods:
        return "I'm sorry to hear that you're feeling " + mood + "."
    else:
        return "I'm sorry, I don't understand that mood. Please try again."