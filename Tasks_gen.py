import random

def create_tasks():

    tasks = [
        'Sing a song aloud',
        'Spend some quality 15 minutes with your loved ones',
        'Go play in the nearby park',
        'Dance to your favourite song',
        'Learn 5 sentences in a new language',
        'Feed the animals like dogs or cats near your home',
        'Meditate for 10 minutes',
        'Practice deep breathing exercises',
        'Take a leisurely walk in nature',
        'Listen to calming music or nature sounds',
        'Write down three things you are grateful for',
        'Spend quality time with loved ones',
        'Practice yoga or gentle stretching',
        'Engage in a creative hobby, like painting or crafting',
        'Read a book that inspires you',
        'Cook a healthy and delicious meal',
        'Practice mindfulness by focusing on the present moment',
        'Declutter and organize your living space',
        'Volunteer your time to help others in need',
        'Watch a feel-good movie or comedy show',
        'Write in a journal about your thoughts and feelings',
        'Go for a scenic drive or bike ride',
        'Spend time in a garden or greenhouse',
        'Do something spontaneous and fun',
        'Practice visualization and imagine your happiest future',
        'reate a vision board with your goals and dreams',
        'Go stargazing on a clear night',
        'Take a power nap to recharge your energy',
        'Spend time in silence and enjoy the peace and quiet',
        'Attend a meditation or mindfulness class',
        'If you have a garden, plant flowers or herbs',
        'Watch the sunrise or sunset',
        'Take a day trip to explore a new place'
    ]

    selected = []

    while len(selected) <= 2:
        i = random.randint(1, 33)
        t = tasks[i]
        if t not in selected:
            selected.append(t)

    return selected

if __name__ == '__main__':

    tasks = create_tasks()    

