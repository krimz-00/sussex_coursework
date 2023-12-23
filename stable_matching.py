preferences_of_men = {
    "Ryan" : ["Lizzy", "Sarah", "Zoey", "Daniella"],
    "Josh" : ["Sarah", "Lizzy", "Daniella", "Zoey"],
    "Blake" : ["Sarah", "Daniella", "Zoey", "Lizzy"],
    "Connor" : ["Lizzy", "Sarah", "Zoey", "Daniella"]
}

preferences_of_women = {
    "Lizzy" : ["Ryan", "Blake", "Josh", "Connor"],
    "Sarah" : ["Ryan", "Blake", "Connor", "Josh"],
    "Zoey" : ["Connor", "Josh", "Ryan", "Blake"],
    "Daniella" : ["Ryan", "Josh", "Connor", "Blake"]
}

#Keeps track of the people who might end up together
tentative_engagements = []

#Keeps track of the men who still need to propose and get accepted to go to the dance
free_men = []

def init_free_men():
    for man in preferences_of_men.keys():
        free_men.append(man)

def match(man):
    print("It's now {}'s turn...".format(man))
    for woman in preferences_of_men[man]:
        taken_match = [couple for couple in tentative_engagements if woman in couple]
        if len(taken_match) == 0:
            tentative_engagements.append([man, woman])
            free_men.remove(man)
            print("{} has found {} to be his prom!".format(man, woman))
            break
        elif len(taken_match) > 0:
            print("{} is already taken!".format(woman))
            current_man = preferences_of_women[woman].index(taken_match[0][0])
            candidate_man = preferences_of_women[woman].index(man)
            if current_man < candidate_man:
                print("She's satisfied with the guy she's with.")
            else:
                print("{} is better than {}".format(man, taken_match[0][0]))
                print("{} is now free again!".format(taken_match[0][0]))
                free_men.remove(man)
                free_men.append(taken_match[0][0])
                taken_match[0][0] = man
                break

def stable_matching():
    while (len(free_men) > 0):
        for man in free_men:
            match(man)
def main():
   init_free_men()
   stable_matching()
   print("The list of the prom couples going to dance together:")
   print(tentative_engagements)

if __name__ == "__main__":
    main()
