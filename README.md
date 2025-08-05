# CS361 Trivia Microservice
Trivia microservice for CS361 that will grab movie trivia from IMDB.com.

Note that this will use libraries flask, requests, and beautifulsoup4 which may need installation:

`pip install flask requests beautifulsoup4`

# How To Request Data
Request data using an HTML GET call. The URL is at /trivia and the default port is 5555 (this can be changed in the file in a variable near the top). The request requires a "title" parameter with a movie title name.

For example:

`http://localhost:5555/trivia?title=Oppenheimer`

You will need to use standard URL encoding for spaces or symbols:

`http://localhost:5555/trivia?title=The%20Dark%20Knight`

You can also use a Python library like requests to handle it for you:

`import requests`

`response = requests.get("http://localhost:5555/trivia", params={"title": "The Dark Knight"})`

# How To Receive Data
Data will be returned in a JSON format with the movie title and all listed trivia under "trivia".

``` json
{
  "title": "The Dark Knight",
  "trivia": [
    "In Sir Michael Caine's opinion, Heath Ledger beat the odds and topped Jack Nicholson's Joker from Batman (1989): \"Jack was like a clown figure, benign but wicked, maybe a killer old uncle. He could be funny and make you laugh. Heath's gone in a completely different direction to Jack, he's like a really scary psychopath. He's a lovely guy and his Joker is going to be a hell of a revelation in this picture.\" Caine bases this belief on a scene where The Joker pays a visit to Bruce Wayne's penthouse. He'd never met Ledger before, so when Ledger arrived and performed, he gave Caine such a fright, he forgot his lines.",
    "In preparation for his role as the Joker, Heath Ledger hid away in a motel room for about six weeks. During this extended stay of seclusion, Ledger delved deep into the psychology of the character. He devoted himself to developing the Joker's every tic, namely the voice and that sadistic-sounding laugh (for the voice, Ledger's goal was to create a tone that didn't echo the work Jack Nicholson did in his 1989 performance as the Joker). Ledger's interpretation of the Joker's appearance was primarily based on the chaotic, disheveled look of punk rocker Sid Vicious combined with the psychotic mannerisms of Malcolm McDowell's character, Alex De Large, from A Clockwork Orange (1971).",
    "While filming a chase scene on Lake Street, the Chicago Police Department received several calls from concerned citizens stating that the police were involved in a vehicle pursuit with a dark vehicle of unknown make or model.",
    "This was the first comic book movie to reach the $1 billion mark worldwide.",
    "The bus crashing backwards into the bank in the opening sequence was much harder to pull off than was anticipated. The bus had to be taken apart and reassembled inside the building (a disused post office), concealed behind a large false wall, and then propelled backwards with an air cannon.",
    "(at around 1h 24 mins) Heath Ledger improvised when he started clapping inside his jail cell in a mocking and sardonic way, as Gordon is promoted. The clapping was not scripted, but Sir Christopher Nolan immediately encouraged the crew to continue filming, and the sequence was included in the final cut.",
    "Heath Ledger directed both homemade videos that The Joker sends to GCN. The first video involving the fake Batman was done under writer, producer, and director Sir Christopher Nolan's supervision. Nolan thought Ledger had done so well with that sequence, he felt there was no need for him to be there when it came time to film the scene where reporter Mike Engel reads The Joker's statement. He put his trust in Ledger and let him do whatever he wanted, ultimately pleased with the result after he'd seen the outcome.",
    "Christian Bale stated in an interview that during the interrogation scene, Heath Ledger wanted him to beat him as hard as he could to get the real feeling of what was required from the scene.",
    "In the early minutes of each movie in the trilogy, the main villain (Ra's al Ghul, The Joker, Bane) disguises himself as one of his own henchmen, and there is a conversation about said villain in each scene.",
    "Cillian Murphy reprises his role as Dr. Jonathan Crane a.k.a. Scarecrow from Batman Begins (2005) in this movie. This makes him the first actor to reprise the role of a Batman villain in the whole film franchise. He also reprises his role in a cameo in The Dark Knight Rises (2012).",
    "Wayne Baker: The IMAX camera technician and consultant has a cameo that is the only close-up shot in the IMAX format in this movie. He sits on the loading dock and reacts to the Batpod emerging from the wreckage of the Batmobile.",
    "Patrick Leahy: (at around 50 mins) The older gentleman that confronts The Joker at the party thrown by Bruce Wayne for Harvey Dent. Senator Leahy is a huge Batman fan, and arranged an early showing of the movie on July 12th, as a fundraiser for the children's section of the Kellogg-Hubbard Library in Montpelier, Vermont. He also appeared in Batman & Robin (1997) and as a Batman: The Animated Series (1992) voice.",
    "Buster Reeves: (at around 1h 16 mins) A Joker thug. He appears in the trailer of The Joker's semi-truck, as he hands The Joker his weapons, and he fires them at the police transport. He then rides in the passenger seat of the cab of the truck as The Joker drives."
  ]
}
```

The standard Python JSON parser will work just fine:

`data = response.json()`

