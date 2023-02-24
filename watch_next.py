import spacy 
nlp = spacy.load('en_core_web_md')

def readMovies(fname : str = "movies.txt"):
    # Read the movie descriptions from local file. 
    movs = []
    descr = []
    with open(fname, 'r') as f: 
        for line in f: 
            l = line.split(':')
            movs.append(l[0]) 
            descr.append(l[1])
    return movs, descr 

def getNextMovie(descr : list[str], lastMovie : str):
    # Find the movie with the highest similarity score with their descriptions
    simScore = [] 
    lm = nlp(lastMovie)
    for d in descr:
        simScore.append(lm.similarity(nlp(d)))
    i = simScore.index(max(simScore))
    return i 

def main(movieName : str, movieDescr : str):
    # Main program function handling the variables and prints 
    movL, descL = readMovies()
    i = getNextMovie(descL, movieDescr)
    print("\nThe next movie you should watch is: ")
    print("-----------------------------------")
    print(movL[i] + " : " + descL[i])
    return

if __name__ == "__main__":
    name = "Planet Hulk"
    descr = """Will he save their world or destroy it? When the Hulk becomes too dangerous 
                for the Earth, the Illuminati trick Hulk into a shuttle and launch him into
                space to a planet where the Hulk can live in peace. Unfortunately, Hulk lands
                on the planer Sakaar where he is sold into slavery and trained as a gladiator."""
    main(name, descr)