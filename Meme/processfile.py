def split_list(lst, element):
    result = []
    sublist = []
    for item in lst:
        if item == element:
            if sublist:
                result.append(sublist)
                sublist = []
        else:
            sublist.append(item)
    if sublist:
        result.append(sublist)
    return result

real = []
newreal = ['7 Damn | wish\n| could read\n', 'Q @ who is justin tim!\n', '= Google\n', 'who is justin timberlake\n', 'ALL NEWS IMAGES VID!\n', 'Justin Timberlake\nAmerican singer-songwriter\n', 'OVERVIEW SONGS ALBUMSï¿½\n', 'Microtransactions in\ngames\n', 'Micro transactions\nfor the entire internet\n', 'fi ay\n', "Don't come to internet tommorow\n", 'WHO WOULD WIN?\n', 'Content creator celebrities with\nmillions of fans and views\n', 'ER\nq!\n', 'One gay boi\n', 'or >\n', 'AS\n&\n', 'Bush\n', 'Shrek (2001)\n', 'Shrek in the Swamp Karaoke\nDance Party (2001)\n', 'Shrek 2 (2004)\n', 'Shrek the Third (2007)\n', 'Obama\n', 'Shrek Forever After (2010)\n)| Puss in Boots (2011)\n', 'Trump\n', 'there have been 0 Shrek\nmovies released during the\nTrump presidency\n', 'Crazy condom fails\n', '"If lanka wasn\'t my daughter, I\'d be dating her. She\'s hot."\n', '"| love incest porn."\n', '"Did we just become best friends?"\n', 'Twitter Support @ @TwitterSupp... - 4c\nWe are pleased to announce that we\nhave given everyone an extra 280\n', 'characters, except Donald Trump, he\nonly gets 11\n', '0 192 11360 O83 a)\n', 'Donald J. Trump @\n@realDonaldTrump\n', 'Replying to @TwitterSupport\nWhat the fu\n', "hello my\ngovernment isn't\ndoing what i told\nit to do\n", 'have you tried\nturning it off and\n', 'on again?\n', 'When your teacher is talking\nabout Java and you remember\n', 'Minecraft was made with Java\n', 'ï¿½)\n', "8 inom I'm something ofa\n", 'when you hit random on the\nSkyrim character creator\n', 'When the teacher talking about\nmarine biology and u just nutted to\ntentacle hentai last night\n', 'fae 4 a aac\n', 'You know, Iï¿½m something of a scientist myself:\n', 'Whatï¿½s more useful?\n', "Ajit Pai A shit pile\na, fertilizes crops VY\nhas practical YW\nuses in landscaping\ndoesn't infringe on\nNS your basic human rights\n", 'Japan before World War II Japan after World War II\n', "It's called hentai,\nand it's art.\n", 'LMAO they made Dumb and Dumber into a real thing\n', "ï¿½Often I'll see advertisements for porn games and they\n", 'say, ï¿½Try Not To Cum,ï¿½ but then when you play the game,\nit seems like the object is to cum. So yes, | would call\nthat bad game design.ï¿½\n', 'ï¿½Shigeru Miyamoto\nOn his revolutionary career at Nintendo\n', 'CLICKH@LE\n', 'Government of the people, by the people,\nfor the people, shall not perish from the\nFarth.\n', '-Abraham Lincoln\n', '| hope | shall possess firmness and virtue\nenough to maintain what | consider the\nmost enviable of all titles, the character of\nan honest man,\n', '-George Washington\n', "I'm, like, really smart.\n-Donald Trump\n", 'Mike pence is trying to have this removed from the\ninternet please share to piss him off\n', "Don't understand why\n", 'ase ere Sate\n', 'Important?\n', 'When you go to bed needing to\ntake a shit but you donï¿½t need to\n', 'when you wake up\n', 'u uN 8 Ok VE D\n', 'when Black Panther is considered a\nturning point for blacks americans\n', "like u didn't just lead the\nfree world for 8 years\n", 'When a nigga with an anime\nprofile pic slides into your DM\n', 't action ow\n', 'IG: @Jedimolestr\nAction Amercan QP \\/ ahve\n', 'American GF Valves\n', 'Pe\n', '\\ spoke with the president of the Virgin Islands\n', ', Lazy Town Memes eee\n) 50mins-@\n', "Stefan Karl deactivated his Twitter account and slowly\nleaving Facebook now. He asked me to tell ya'll that he\nwill always remember you guys, he loves you and will\nnever let you down but now he's going to focus on\ntrying to extend his life as much as he can and enjoy\nlife with his kids, wife and family.\n", 'ï¿½Follow your dreams and know that death is nothing,\nlife is everything."\n', 'Sincerely yours, Milena Barshatskaya Art\n#wearenumberone <3\n', 'Top 10 Pranks That went too\n', 'Far\n2.6M views\n', "When you're stationed at an air\nbase in Syria and all of the\nRussians just get up and leave\n", 'The intent was to provide the kids with a sense of\naccomplishment for unlocking different positions\n', 'Third grade niggas when somebody randomly\nopens the textbook to the right page\n', 'He looks like\nhis father\n', 'When you joke about 9/11 in 2001\nand everyone hates you\n', 're ï¿½\n', 'im\n=\n', 'but your kidsiare g\n', 'take a tide pod at the\n', 'same time\nto see who dies first\n', '% ï¿½ aï¿½\n', 'Now this is pod-racing!\n', 'Sie, ice a yy\neit yall ae\nHF 4\nBe "4\n', "ï¿½I became fat so when I look,\ndown while jerking off, I don't\nsee my dick, because that would\nbe gay.ï¿½\n", '-him Jong Un\n']

"""
with open("meme.txt", "r") as memeread:
    real = split_list(memeread, "\n")
"""

for item in newreal:
    real.append("".join(item).replace("\n", ""))

with open("meme.txt", "w") as memewrite:
    for item in real:
        memewrite.write(item+"\n")

