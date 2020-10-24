import pickle

def leaderboard_en():
    with open('rank.pickle', 'rb') as f:
        rank = pickle.load(f)
        print(rank)
        
def saving(nick, counter):
    bestscores={}
    bestscores.update({nick : counter})
    with open('rank.pickle', 'ab') as f:
        pickle.dump(bestscores, f, pickle.HIGHEST_PROTOCOL)
    print("Saving...")

nick=input("nick: ")
counter=input("counter: ")
counter=int(counter)

saving(nick, counter)
leaderboard_en()
