#Books and References program: 'LIKEREAD'
import random
import csv

def username():
        global user
        user=str(input("Enter Username: ")).strip()
        us1=[]
        with open("user.csv","r+",newline='\r\n') as f1:
            u_reader=csv.reader(f1)
            for r in u_reader:
                if r:
                    us1.append(str(r[0]).lower())
            if user.lower() in  us1:
                print("Username already chosen choose another one")
                username()
        return user 
def sign_up():   
    global user
    user=username()
    password=input("Enter Password: ")
    f1=open("user.csv","a+")
    u_writer=csv.writer(f1)
    u_writer.writerow([user.lower(),password])
    f1.flush()
    print('You are now registered. You may proceed.\n ')
    return user

def login():
    global user
    a=True
    user=str(input("Enter Username: ")).strip()
    password=input("Enter Password: ")
    with open("user.csv","r+",newline='\r\n') as f1:
        u_reader=csv.reader(f1)
        for r in u_reader:
            if r==[user.lower(),password]:
                print("You may proceed\n")
                a=False
        if a==True:
            print("Credentials don't match, Please try again")
            login()
    return user

print('WELCOME TO LIKEREAD! ') #Line 1
print()

def write(x):    
    with open("library.csv","a+",newline='\r\n') as f1:
        print('''Genres:
Enter 1 for Classics
Enter 2 for Fantasy
Enter 3 for Sci-fi
Enter 4 for Romance
Enter 5 for Suspense and Thrillers
Enter 6 for Biographies and Autobiographies ''')        
        b=True
        li=[]
        while b:
            genre=input("Enter genre number: ")
            if genre=='1':
                genre="Classics"
            elif genre=='2':
                genre="Fantasy"
            elif genre=='3':
                genre="Sci-Fi"
            elif genre=='4':
                genre="Romance"
            elif genre=='5':
                genre="Suspense and Thriller"
            elif genre=='6':
                genre="Autobiography/Biography"
            book=input("Enter book name: ")
            status=input('''Enter 1 for TBR (To Be Read)
Enter 2 for already read
Enter:''')
            if status=='1':
                status="TBR"
            elif status=='2':
                status="Already Read"                            
            li=[x,genre,book,status]        
            u_writer=csv.writer(f1)
            u_writer.writerow(li)
            ans=input("Do you want to enter more? Enter yes/no: ")
            if ans.lower()=="no":
                b=False
            elif ans.lower()=='yes':
                continue
            else:
                print('INVALID INPUT. Try again.')

def read(x):
    
    print('''Genres:
Enter 1 for Classics
Enter 2 for Fantasy
Enter 3 for Sci-fi
Enter 4 for Romance
Enter 5 for Suspense and Thrillers
Enter 6 for Biographies and Autobiographies ''') 
    with open("library.csv","r",newline='\r\n') as f1:
        u_reader=csv.reader(f1)
        a=True
        while a:
            genre=input("Enter genre number: ")
            status=input('''Enter 1 for TBR (To Be Read)
Enter 2 for already read
Enter:''')  
            if status=='1':
                status="TBR"
            elif status=='2':
                status="Already Read"
                
            if genre=='1':
                genre="Classics"
            elif genre=='2':
                genre="Fantasy"
                    
            elif genre=='3':
                genre="Sci-Fi"
                    
            elif genre=='4':
                genre="Romance"
                     
            elif genre=='5':
                genre="Suspense and Thriller"
                    
            elif genre=='6':
                genre="Autobiography/Biography"
            imp=False
            f1.seek(0)
            for r in u_reader:
                if r:
                    if r[1]==genre and r[3]==status and r[0]==x:
                        print(r[2])
                        imp=True
            if imp==False:
                print('Something went wrong')
            ans=input("Do you wanna try again? Yes/No?: ")
            if ans.lower()=="no":
                a=False
            elif ans.lower()=='yes':
                continue
            else:
                print('INVALID INPUT. Try again.')


print('''Enter 1 to register
Enter 2 to login''')  # Line 2

a=True
while a:              
    ans=input("Enter number: ")   # Line 3 
    if ans=='1':
        sign_up()
        a=False
    elif ans=='2':
        login()
        a=False
    else:
        print("invalid input")
print('''You may either add books in your library or check out all  
the books in it''')                   # Line 4
l=input('''Enter 1 to create/append in your library.
Enter 2 for reading it.
Enter any other character to use the novel suggestor.
Enter: ''')                   # Line 5
if l=='1':
    write(user)
elif l=='2':
    read(user)

           
print('''LIKEREAD: THE BEST SUGGESTION GENERATOR FOR NOVELS''')   # Line 6
print('''\n Here you will get the best suggestions with brief and ratings''') 
# Line 7

print('''\nEnter the required number of your genre:
Enter 1 for Classics
Enter 2 for Fantasy
Enter 3 for Sci-fi
Enter 4 for Romance
Enter 5 for Suspense and Thrillers
Enter 6 for Biographies and Autobiographies \n''')    # Line 8

#CLASSICS
li1=['''Pride and Prejudice by Jane Austen : (rating : 4.27/5)
Since its immediate success in 1813,Pride and Prejudice has remained one of
the most popular novels in the English language. Jane Austen called this
brilliant work "her own darling child"and its vivacious heroine, Elizabeth
Bennet, "as delightful a creature as ever appeared in print." The romantic
clash between the opinionated Elizabeth and her proud beau, Mr. Darcy, is a
splendid performance of civilized sparring. And Jane Austen's radiant wit
bsparkles as her characters
dance a delicate quadrille of flirtation and intrigue, making this book the
most superb comedy of manners of Regency England''',
     '''Wuthering Heights by Emily Bronte: (rating:3.87)
This best-selling Norton Critical Edition is based on the 1847 first edition of
the novel. For the Fourth Edition, the editor has collated the 1847 text with
several modern editions and has corrected a number of variants, including
accidentals. The text is accompanied by entirely new explanatory annotations.

New to the fourth Edition are twelve of Emily Bronte's letters regarding the
publication of the 1847 edition of Wuthering Heights as well as the evolution
of the 1850 edition, prose and poetry selections by the author, four reviews of
the novel, and poetry selections by the author, four reviews of the novel, and
Edward Chitham's insightful and informative chronology of the creative process
behind the beloved work.

Five major critical interpretations of Wuthering Heights are included, three of
them new to the Fourth Edition. A Stuart Daley considers the importance of
chronology in the novel. J. Hillis Miller examines Wuthering Heights's problems
of genre and critical reputation. Sandra M. Gilbert assesses the role of
Victorian Christianity plays in the novel, while Martha Nussbaum traces the
novel's romanticism. Finally, Lin Haire-Sargeant scrutinizes the role of
Heathcliff in film adaptations of Wuthering Heights.

A Chronology and updated Selected Bibliography are also included.''',
     '''To Kill a Mockingbird by Harper Lee: (rating:4.27)
The unforgettable novel of a childhood in a sleepy Southern town and the
crisis of conscience that rocked it. "To Kill A Mockingbird" became both an
instant bestseller and a critical success when it was first published in 1960.
It went on to win the Pulitzer Prize in 1961 and was later made into an Academy
Award-winning film, also a classic.

Compassionate, dramatic, and deeply moving, "To Kill A Mockingbird" takes
readers to the roots of human behavior - to innocence and experience, kindness
and cruelty, love and hatred, humor and pathos. Now with over 18 million copies
in print and translated into forty languages, this regional story by a young
Alabama woman claims universal appeal. Harper Lee always considered her book
to be a simple love story. Today it is regarded as a masterpiece of American
literature.''', '''Jane Eyre by Charlotte Brontë: (rating: 4.14)
Orphaned as a child, Jane has felt an outcast her whole young life. Her courage
is tested once again when she arrives at Thornfield Hall, where she has been
hired by the brooding, proud Edward Rochester to care for his ward Adèle. Jane
finds herself drawn to his troubled yet kind spirit. She falls in love. Hard.

But there is a terrifying secret inside the gloomy, forbidding Thornfield Hall.
Is Rochester hiding from Jane? Will Jane be left heartbroken and exiled once
again?''', '''A Tale of Two Cities by Charles Dickens: (rating: 3.86)
A Tale of Two Cities is Charles Dickens’s great historical novel, set against
the violent upheaval of the French Revolution. The most famous and perhaps the
most popular of his works, it compresses an event of immense complexity to the
scale of a family history, with a cast of characters that includes a
bloodthirsty ogress and an antihero as believably flawed as any in modern
fiction. Though the least typical of the author’s novels, A Tale of Two Cities
still underscores many of his enduring themes—imprisonment, injustice, social
anarchy, resurrection, and the renunciation that fosters renewal. ''']

#FANTASY
li2=['''The Cruel Prince by Holly Black: (rating: 4.09)
First in the bestselling Folk of the Air trilogy. The sequels - The Wicked
King and The Queen of Nothing - are the winners of/won the Goodreads YA Best
Fantasy in 2019 and 2020. Nominated for the CILIP CARNEGIE MEDAL 2019.
Winner of the silver INKY for best international YA book.

"A dark jewel of a book . . . intoxicating" - Leigh Bardugo,#1 New York Times
bestselling author of Six of Crows.
     
Of course I want to be like them.
They're beautiful as blades forged in some divine fire. 
They will live forever. And Cardan is even more beautiful than the rest. 
I hate him more than all the others.
I hate him so much that sometimes when I look at him, I can hardly breathe.
One terrible morning, Jude and her sisters see their parents murdered in front
of them. The terrifying assassin abducts all three girls to the world of Faerie,
where Jude is installed in the royal court but mocked and tormented by the
Faerie royalty for being mortal. As Jude grows older, she realises that she
will need to take part in the dangerous deceptions of the fey to ever truly
belong. But the stairway to power is fraught with shadows and betrayal. And
looming over all is the infuriating, arrogant and charismatic Prince Cardan . .
Dramatic and thrilling fantasy blends seamlessly with enthralling storytelling
to create a fully realised and seductive world, brimful of magic and romance.''',
     '''A Court of Thorns and Roses by  Sarah J. Maas: (rating 4.18)
Perfect for fans of Kristin Cashore and George R.R. Martin, this first book in
an action-packed new series is impossible to put down!

When nineteen-year-old huntress Feyre kills a wolf in the woods, a beast-like
creature arrives to demand retribution for it. Dragged to a treacherous magical
land she only knows about from legends, Feyre discovers that her captor is not
an animal, but Tamlin-- one of the lethal, immortal faeries who once ruled
their world. As she dwells on his estate, her feelings for Tamlin transform
from icy hostility into a fiery passion that burns through every lie and warning
she's been told about the beautiful, dangerous world of the Fae. But an ancient,
wicked shadow over the faerie lands is growing, and Feyre must find a way to
stop it . . . or doom Tamlin--and his world--forever.''',  
''' Red Queen (Red Queen #1) by Victoria Aveyard: (rating: 4.03)
Red Queen is a young adult fantasy novel written by American writer Victoria
Aveyard. Published in February 2015, it was her first novel and first series.
Aveyard followed up with three sequels: Glass Sword, King's Cage and War Storm.
Red Queen won the 2015 Goodreads Choice Award for Debut Goodreads Author and
was nominated for the 2015 Goodreads Choice Award for Young Adult Fantasy &
Science Fiction.
This is a world divided by blood—red or silver. The Reds are commoners, ruled
by a Silver elite in possession of god-like superpowers. And to Mare Barrow, a
seventeen-year-old Red girl from the poverty-stricken Stilts, it seems like
nothing will ever change. That is until she finds herself working in the Silver
Palace. Here, surrounded by the people she hates the most, Mare discovers that,
despite her red blood, she possesses a deadly power of her own. One that
threatens to destroy the balance of power. Fearful of Mare's potential, the
Silvers hide her in plain view, declaring her a long-lost Silver princess, now
engaged to a Silver prince. Despite knowing that one misstep would mean her
death, Mare works silently to help the Red Guard, a militant resistance group,
and bring down the Silver regime. But this is a world of betrayal and lies, and
Mare has entered a dangerous dance—Reds against Silvers, prince against prince,
and Mare against her own heart. ''',
''' See the Grishaverse come to life on screen with Shadow and Bone, now a
Netflix original series. Discover what comes next for heist trio Kaz, Inej,
and Jesper -- and the star-crossed Nina and Matthias -- in the #1 New York
Times bestseller Six of Crows, Book One of the Six of Crows Duology. Ketterdam:
a bustling hub of international trade where anything can be had for the right
price―and no one knows that better than criminal prodigy Kaz Brekker. Kaz is
offered a chance at a deadly heist that could make him rich beyond his wildest
dreams. But he can't pull it off alone. . . .

A convict with a thirst for revenge.

A sharpshooter who can't walk away from a wager.

A runaway with a privileged past.

A spy known as the Wraith.

A Heartrender using her magic to survive the slums.

A thief with a gift for unlikely escapes.

Six dangerous outcasts. One impossible heist. Kaz's crew is the only thing
that might stand between the world and destruction―if they don't kill each
other first. Six of Crows by Leigh Bardugo returns to the breathtaking world of
the Grishaverse in this unforgettable tale about the opportunity―and the
adventure―of a lifetime.''',
''' City of Bones by Cassandra Clare : (rating: 4.08) 
City of Bones, the first installment in the bestselling The Mortal Instruments
series, introduces readers to the world of Shadowhunters, a powerful line of
human-angel hybrids secretly living—and slaying demons—alongside “mundanes,” or
normal humans. But it’s the saga’s third entry that dramatically raises the
stakes of teenage protagonists Clary Fray and Jace Wayland’s struggle to prevent
the evil Valentine Morgenstern from creating a dark new order of otherworldly
warriors. In the midst of a young adult fantasy boom, it was Cassandra Clare’s
ability to capture the beauty and pain of young love—for heroes of varied sexual
identities—coupled with her flair for the supernatural that distinguished her
books from the pack. Since completing the first three volumes of The Mortal
Instruments, Clare has expanded her Shadowhunters universe to include four
other series—for a current total of 15 novels—as well as a number of short story
collections, companion books and graphic novels.''']
 

#SCI-FI
li3=[''' Blindsight by Peter Watts: (rating: 4.35 )
First contact between humanity and an extraterrestrial civilization are a
cornerstone of science fiction, ranging from aliens with funny noses to the
genuinely alien. Peter Watts’ novel Blindsight stars after the planet is
bombarded by a strange cluster of objects that release a single broadcast before
going dark. When scientists receive another transmission from a comet outside
of the solar system, they dispatch an expedition composed of five trans-human
specialists, including a vampire. What they discover is indeed alien: a sort
of hive-mind intelligence that’s part of a much larger diaspora. Where many
science fiction adventures deal with humanity’s introduction to a galactic
civilization in which we become an equal partner/citizen, Watts posits
something far stranger: interstellar intelligence that’s genuinely alien, and
to which humanity is providing to be a major nuisance and threat. It’s a
groundbreaking novel that helped break authors away from human analogs and into
more stranger, introspective territory about our place in the cosmos.''',
'''THE HUNGER GAMES BY SUZANNE COLLINS : (rating:4.32 )
Adult and YA science fiction are often marketed to very different audiences,
with both sides looking down on the other. It’s a nonsensical barrier, and
Suzanne Collins’ book The Hunger Games is a good demonstration that the YA
designation doesn’t necessarily mean that an author is talking down to its
audience.

Set in a dystopic future where the United States has collapsed and been
replaced with Panem, children are selected for a brutal competition every ten
years from each of the country’s twelve districts, in which they fight to the
death, as punishment for a failed revolution.In the ruins of a placeonce known
as North America lies the nation of Panem, a shining Capitol surrounded by
twelve outlying districts. The Capitol is harsh and cruel and keeps the
districts in line by forcing them all to send one boy and one girl between the
ages of twelve and eighteen to participate in the annual Hunger Games, a fight
to the death on live TV.Sixteen-year-old Katniss Everdeen, who lives alone with
her mother and younger sister, regards it as a death sentence when she steps
forward to take her sister's place in the Games. But Katniss has been close to
dead before—and survival, for her, is second nature. Without really meaning
to, she becomes a contender. But if she is to win, she will have to start
making choices that weight survival against humanity and life against love.

Collins’ book deals with pressing issues of brutality and trauma, as well as
wealth inequality, poverty, and revolution. With its release in 2008, the book
became a major bestseller and media franchise, and unleashed a floodgate of
dystopian-themed YA novels that explored the darker parts of modern society.''',
''' The Windup Girl By Paolo Bacigalupi: (rating: 3.7)
Between major hurricanes, widespread wildfires, and a global temperature that
keeps rising, climate change is at the forefront of the public’s consciousness
in the last decade. While the issue was certainly settled in 2009, Paolo
Bacigalupi’s The Windup Girl was a breakthrough for science fiction by putting
a world with a drastically changed climate front and center.

Set in a world where oil is no longer a thing and where mega agricorps control
the world’s food supply with genetically modified crops, Bacigalupi’s story is
set in a futuristic Thailand that’s managed to stave off environmental
apocalypse: because the country has been able to keep outsiders out, it’s
avoided crop failures and famine. That success however, comes with problems:
Agents from some of those agricorps are working to get their hands on the
country’s seedbank to solve some of their problems, while a genetically-modified
woman tries to escape sexual slavery as war looms.

Climate change is a subject that’s ripe for fiction, but Bacigalupi goes beyond
mere disaster porn with this novel. The Windup Girl looks at how rampant
capitalism and its associated abuses underpins the climate disaster.''',
'''1984 by George Orwell: (rating: 4.19)
Among the seminal texts of the 20th century, Nineteen Eighty-Four is a rare
work that grows more haunting as its futuristic purgatory becomes more real.
Published in 1949, the book offers political satirist George Orwell's
nightmarish vision of a totalitarian, bureaucratic world and one poor stiff's
attempt to find individuality. The brilliance of the novel is Orwell's
prescience of modern life—the ubiquity of television, the distortion of the
language—and his ability to construct such a thorough version of hell. Required
reading for students since it was published, it ranks among the most terrifying
novels ever written. 1984: A Novel, unleashes a unique plot as per which No One
is Safe or Free. No place is safe to run or even hide from a dominating party
leader, Big Brother, who is considered equal to God. This is a situation where
everything is owned by the State. The world was seeing the ruins of World War II. 
Leaders such as Hitler, Stalin and Mussolini prevailed during this phase. Big
Brother is always watching your actions. He even controls everyone?s feelings
of love, to live and to discover. The basic plot of this historic novel
revolves around the concept that no person has freedom to live life on his or
her own terms. The present day is 1984.
The whole world is gradually changing. The nations which enjoy freedom, have
distorted into unpleasant and degraded places, in turn creating a powerful
cartel known as Oceania. This is the world where the Big Brother controls
everything. There is another character Winston Smith, who is leading a normal
layman life under these harsh circumstances, through hating all of this. He
works on writing the old newspaper articles in order to make history or past
relevant to today's party line. He is efficient enough in spite of hating his
bosses. Julia, a young girl who is morally very rigid comes into the fore. She
too hates the system as much as Winston does. Gradually, they get into an
affair but have to conceal their feelings for each other, as it will not be
acceptable by Big Brother. In Big Brother's bad world, freedom is slavery and
ignorance is strength.  ''',
 ''' The Sorority Murder by Allison Brennan: (rating: 3.95 )
A popular sorority girl. An unsolved murder. A campus podcast with chilling
repercussions. Lucas Vega is obsessed with the death of Candace Swain, who left
a sorority party one night and nevercame back. Her body was found after two
weeks, but the case has grown cold. Three years later while 
interning at the medical examiner's, Lucas discovers new information, but the
police are not interested. Lucas knows he has several credible pieces of the
puzzle. He just isn't sure how they fit together. So he creates a podcast to
revisit Candace's last hours. Then he encourages listeners to crowdsource what
they remember and invites guest lecturer Regan Merritt, a former US marshal,
to come on and share her expertise.
New tips come in that convince Lucas and Regan they are onto something. Then
shockingly one of the podcast callers turns up dead. Another hints at Candace's
secret life, a much darker picture than Lucas imagined--and one that implicates
other sorority sisters. Regan uses her own resources to bolster their theory 
and learns that Lucas is hiding his own secret. The pressure is on to solve the
murder, but first Lucas must come clean about his real motives in pursuing
this podcast--before the killer silences him forever.

"Fans of Jeff Abbott and Karin Slaughter will find this crime novel hard to put
down."-- Publishers Weekly on The Third to Die
"Downright spectacular... [A] riveting page turner as prescient as it is
purposeful." --Providence Journal on Tell No Lies''']

#ROMANCE
li4=['''The Fault in Our Stars by John Green: (rating: 4.17)
Despite the tumor-shrinking medical miracle that has bought her a few years,
Hazel has never been anything but terminal, her final chapter inscribed upon
diagnosis. But when a gorgeous plot twist named Augustus Waters suddenly 
appears at Cancer Kid Support Group, Hazel's story is about to be completely 
rewritten.

Insightful, bold, irreverent, and raw, The Fault in Our Stars is award-winning
author John Green's most ambitious and heartbreaking work yet, brilliantly
exploring the funny, thrilling, and tragic business of being alive and in love.
''','''To All the Boys I've Loved Before by Jenny Han: (rating: 4.09)
To All the Boys I’ve Loved Before is the story of Lara Jean, who has never
openly admitted her crushes, but instead wrote each boy a letter about how she
felt, sealed it, and hid it in a box under her bed.

But one day Lara Jean discovers that somehow her secret box of letters has been
mailed, causing all her crushes from her past to confront her about the 
letters: her first kiss, the boy from summer camp, even her sister's 
ex-boyfriend, Josh.

As she learns to deal with her past loves face to face, Lara Jean discovers
that something good may come out of these letters after all.''',
     '''Thirteen Reasons Why by Jay Asher: (Rating: 3.88)
You can’t stop the future.
You can’t rewind the past.
The only way to learn the secret . . . is to press play.

Clay Jensen returns home from school to find a strange package with his name on
it lying on his porch. Inside he discovers several cassette tapes recorded by
Hannah Baker–his classmate and crush–who committed suicide two weeks earlier.
Hannah’s voice tells him that there are thirteen reasons why she decided to end
her life. Clay is one of them. If he listens, he’ll find out why.

Clay spends the night crisscrossing his town with Hannah as his guide. He
becomes a firsthand witness to Hannah’s pain, and as he follows Hannah’s
recorded words throughout his town, what he discovers changes his life forever.
''','''The DUFF: Designated Ugly Fat Friend by Kody Keplinger: (Rating: 3.81)
Seventeen-year-old Bianca Piper is cynical and loyal, and she doesn't think
she's the prettiest of her friends by a long shot. She's also way too smart to
fall for the charms of man-slut and slimy school hottie Wesley Rush. In fact,
Bianca hates him. And when he nicknames her "the Duff," she throws her Coke in
his face.

But things aren't so great at home right now, and Bianca is desperate for a
distraction. She ends up kissing Wesley. Worse, she likes it. Eager for escape,
Bianca throws herself into a closeted enemies-with-benefits relationship with
him.

Until it all goes horribly awry. It turns out Wesley isn't such a bad listener,
and his life is pretty screwed up, too. Suddenly Bianca realizes with absolute
horror that she’s falling for the guy she thought she hated more than anyone.''',
     '''Beautiful Disaster by Jamie McGuire: (rating: 4.07)
The new Abby Abernathy is a good girl. She doesn’t drink or swear, and she has
the appropriate number of cardigans in her wardrobe. Abby believes she has
enough distance from the darkness of her past, but when she arrives at college
with her best friend, her path to a new beginning is quickly challenged by
Eastern University's Walking One-Night Stand.

Travis Maddox, lean, cut, and covered in tattoos, is exactly what Abby needs—
and wants—to avoid. He spends his nights winning money in a floating fight ring,
and his days as the ultimate college campus charmer. Intrigued by Abby’s
resistance to his appeal, Travis tricks her into his daily life with a simple
bet. If he loses, he must remain abstinent for a month. If Abby loses, she
must live in Travis’s apartment for the same amount of time. Either way, Travis
has no idea that he has met his match.''']

#SUSPENSE AND THRILLERS
li5=['''Verity by Colleen Hoover : (rating: 4.39 )
A "sublimely creepy" psychological thriller from #1 New York Times bestselling
author Colleen Hoover (Tarryn Fisher, New York Times bestselling author).

Lowen Ashleigh is a struggling writer on the brink of financial ruin when she
accepts the job offer of a lifetime. Jeremy Crawford, husband of bestselling
author Verity Crawford, has hired Lowen to complete the remaining books
in a successful series his injured wife is unable to finish.
Lowen arrives at the Crawford home, ready to sort through years of Verity’s
notes and outlines, hoping to find enough material to get her started. What
Lowen doesn’t expect to uncover in the chaotic office is an unfinished
autobiography Verity never intended for anyone to read. Page after page of
bone-chilling admissions, including Verity's recollection of the night her
family was forever altered. Lowen decides to keep the manuscript hidden from
Jeremy, knowing its contents could devastate the already grieving father. But
as Lowen’s feelings for Jeremy begin to intensify, she recognizes all the ways
she could benefit if he were to read his wife’s words. After all, no matter how
devoted Jeremy is to his injured wife, a truth this horrifying would make it
impossible for him to continue loving her. ''',
'''I Am Not Who You Think I Am by Eric Rickstad : (rating: 3.61)
Wayland Maynard is just eight years old when he sees his father kill himself,
finds a note that reads I am not who you think I am, and is left reeling with
grief and shock. Who was his father if not the loving man Wayland knew?
Terrified, Wayland keeps the note a secret, but his reasons for being afraid
are just beginning.

Eight years later, Wayland makes a shocking discovery and becomes certain the
note is the key to unlocking a past his mother and others in his town want to
keep buried.With the help of two friends, Wayland searches for the truth.
Together they uncover strange messages scribbled in his father's old books, a
sinister history behind the town's most powerful family, and a bizarre tragedy
possibly linked to Wayland's birth. Each revelation raises more questions and
deepens Wayland's suspicions of everyone around him. Soon, he'll regret he ever
found the note, trusted his friends, or believed in such a thing as the truth.

I Am Not Who You Think I Am is an ingenious, addictive, and shattering tale of
grief, obsession, and fate as eight words lead to lifetimes of ruin. ''',
'''Apples Never Fall by Liane Moriarty: (rating: 3.89 )
From Liane Moriarty, the number one New York Times best-selling author of Big
Little Lies and Nine Perfect Strangers, comes Apples Never Fall, an audiobook
that looks at marriage, siblings, and how the people we love the most can hurt
us the deepest.

The Delaney family love one another dearly - it’s just that sometimes they want
to murder each other.... If your mother was missing, would you tell the police?
Even if the most obvious suspect was your father? This is the dilemma facing
the four grown Delaney siblings. The Delaneys are fixtures in their community.
The parents, Stan and Joy, are the envy of all of their friends. They’re killers
on the tennis court, and off it their chemistry is palpable. But after 50 years
of marriage, they’ve finally sold their famed tennis academy and are ready to
start what should be the golden years of their lives. So why are Stan and Joy
so miserable?

The four Delaney children - Amy, Logan, Troy, and Brooke - were tennis stars in
their own right, yet as their father will tell you, none of them had what it
took to go all the way. But that’s okay, now that they’re all successful grown-
ups and there is the wonderful possibility of grandchildren on the horizon.

One night a stranger named Savannah knocks on Stan and Joy’s door, bleeding
after a fight with her boyfriend. The Delaneys are more than happy to give her
the small kindness she sorely needs. If only that was all she wanted.Later,
when Joy goes missing, and Savannah is nowhere to be found, the police question
the one person who remains: Stan. But for someone who claims to be innocent, he,
like many spouses, seems to have a lot to hide. Two of the Delaney children
think their father is innocent, two are not so sure - but as the two sides
square off against each other in perhaps their biggest match ever, all of the
Delaneys will start to reexamine their shared family history in a very new light.''',
'''The Whistler (The Whistler #1) by John Grisham: (rating: 3.89) 
We expect our judges to be honest and wise. Their integrity and impartiality are
the bedrock of the entire judicial system. We trust them to ensure fair trials,
to protect the rights of all litigants, to punish those who do wrong, and to
oversee the orderly and efficient flow of justice.But what happens when a judge
bends the law or takes a bribe? It’s rare, but it happens.

Lacy Stoltz is an investigator for the Florida Board on Judicial Conduct. She
is a lawyer, not a cop, and it is her job to respond to complaints dealing with
judicial misconduct. After nine years with the Board, she knows that most
problems are caused by incompetence, not corruption.But a corruption case
eventually crosses her desk. A previously disbarred lawyer is back in business
with a new identity. He now goes by the name Greg Myers, and he claims to know
of a Florida judge who has stolen more money than all other crooked judges
combined. And not just crooked judges in Florida. All judges, from all states,
and throughout U.S. history. What’s the source of the ill-gotten gains? It seems
the judge was secretly involved with the construction of a large casino on
Native American land. The Coast Mafia financed the casino and is now helping
itself to a sizable skim of each month’s cash. The judge is getting a cut and
looking the other way. It’s a sweet deal: Everyone is making money.
But now Greg wants to put a stop to it. His only client is a person who knows
the truth and wants to blow the whistle and collect millions under Florida law.
Greg files a complaint with the Board on Judicial Conduct, and the case is
assigned to Lacy Stoltz, who immediately suspects that this one could be
dangerous. Dangerous is one thing. Deadly is something else.''',
'''A Good Girl's Guide to Murder : (rating: 4.37) 
A debut YA crime thriller as addictive as Serial and as page-turning as One of
Us Is Lying.

A cold-case thriller written in the original format of a college report -
complete with interviews, logs and murder maps.

A deftly-woven cold-case plot with themes of race, privilege, family and justice
at its heart.

An incredibly commercial, thrilling and darkly humorous debut voice in YA crime
fiction from a young author who is One To Watch.

The case is closed. Five years ago, schoolgirl Andie Bell was murdered by Sal
Singh. The police know he did it. Everyone in town knows he did it.But having
grown up in the same small town that was consumed by the murder, Pippa Fitz-
Amobi isn't so sure. When she chooses the case as the topic for her final year
project, she starts to uncover secrets that someone in town desperately wants
to stay hidden. And if the real killer is still out there, how far will they
go to keep Pip from the truth?  
Perfect for fans of One of Us Is Lying, We Were Liars, Gone Girl, PrettyLittle
Liars and Riverdale.''']

#BIOGRAPHIES AND AUTOBIOGRAPHIES
li6=['''The Diary of a Young Girl by Anne Frank: (rating: 4.17)
Discovered in the attic in which she spent the last years of her life, Anne
Frank’s remarkable diary has become a world classic—a powerful reminder of the
horrors of war and an eloquent testament to the human spirit.

In 1942, with the Nazis occupying Holland, a thirteen-year-old Jewish girl and
her family fled their home in Amsterdam and went into hiding. For the next two
years, until their whereabouts were betrayed to the Gestapo, the Franks and
another family lived cloistered in the “Secret Annexe” of an old office
building. Cut off from the outside world, they faced hunger, boredom, the
constant cruelties of living in confined quarters, and the ever-present threat
of discovery and death. In her diary Anne Frank recorded vivid impressions of
her experiences during this period. By turns thoughtful, moving, and
surprisingly humorous, her account offers a fascinating commentary on human
courage and frailty and a compelling self-portrait of a sensitive and spirited
young woman whose promise was tragically cut short.''',
     '''Long Walk to Freedom by Nelson Mandela: (rating: 4.29)
Nelson Mandela is one of the great moral and political leaders of our time: an
international hero whose lifelong dedication to the fight against racial
oppression in South Africa won him the Nobel Peace Prize and the presidency of
his country.

Since his triumphant release in 1990 from more than a quarter-century of
imprisonment, Mandela has been at the center of the most compelling and
inspiring political drama in the world. As president of the African National
Congress and head of South Africa's anti-apartheid movement, he was instrumental
in moving the nation toward multiracial government and majority rule. He is
revered everywhere as a vital force in the fight for human rights and racial
equality.

The foster son of a Thembu chief, Mandela was raised in the traditional, tribal
culture of his ancestors, but at an early age learned the modern, inescapable
reality of what came to be called apartheid, one of the most powerful and
effective systems of oppression ever conceived. In classically elegant and
engrossing prose, he tells of his early years as an impoverished student and
law clerk in a Jewish firm in Johannesburg, of his slow political awakening,
and of his pivotal role in the rebirth of a stagnant ANC and the formation of
its Youth League in the 1950s.

He describes the struggle to reconcile his political activity with his devotion
to his family, the anguished breakup of his first marriage, and the painful
separations from his children. He brings vividly to life the escalating
political warfare in the fifties between the ANC and the government, culminating
in his dramatic escapades as an underground leader and the notorious Rivonia
Trial of 1964, at which he was sentenced to life imprisonment. Herecounts the
surprisingly eventful twenty-seven years in prison and the complex, delicate
negotiations that led both to his freedom and to the beginning of the end of
apartheid. Finally he provides the ultimate inside account.''',
     '''The Story of My Life by Helen Keller: rating:4.06)
When she was 19 months old, Helen Keller (1880–1968) suffered a severe illness
that left her blind and deaf. Not long after, she also became mute. Her
tenacious struggle to overcome these handicaps-with the help of her inspired
teacher, Anne Sullivan-is one of the great stories of human courage and
dedication. In this classic autobiography, first published in 1903, Miss Keller
recounts the first 22 years of her life, including the magical moment at the
water pump when, recognizing the connection between the word "water" and the
cold liquid flowing over her hand, she realized that objects had names.
Subsequent experiences were equally noteworthy: her joy at eventually learning
to speak, her friendships with Oliver Wendell Holmes, Edward Everett Hale and
other notables, her education at Radcliffe (from which she graduated cum laude),
and-underlying all-her extraordinary relationship with Miss Sullivan, who showed
a remarkable genius for communicating with her eager and quick-to-learn pupil.''',
     '''Mary Queen of Scots by Antonia Fraser: (Rating: 3.89)
She was the quintessential queen: statuesque, regal, dazzlingly beautiful.Her
royal birth gave her claim to the thrones of two nations; her marriage to the
young French dauphin promised to place a third glorious crown on her noble head.
Instead, Mary Stuart became the victim of her own impulsive heart, scandalizing
her world with a foolish passion that would lead to abduction, rape, and even
murder. Betrayed by those she most trusted, she would be lured into a deadly
game of power, only to lose to her envious and unforgiving cousin, Elizabeth I.
Here is her story, a queen who lost a throne for love, a monarch pampered and
adored even as she was led to her beheading, the unforgettable woman who became
a legend for all time.''',
     '''Cleopatra: A Life by Stacy Schiff: (rating:3.70)
The Pulitzer Prize-winning biographer brings to life the most intriguing woman
in the history of the world: Cleopatra, the last queen of Egypt.

Her palace shimmered with onyx, garnets, and gold, but was richer still in
political and sexual intrigue. Above all else, Cleopatra was a shrewd strategist
and an ingenious negotiator.

Though her life spanned fewer than forty years, it reshaped the contours of the
ancient world. She was married twice, each time to a brother. She waged a
brutal civil war against the first when both were teenagers. She poisoned the
second. Ultimately she dispensed with an ambitious sister as well; incest and
assassination were family specialties. Cleopatra appears to have had intercourse
with only two men. They happen, however, to have been Julius Caesar and Mark
Antony, among the most prominent Romans of the day. Both were married to other
women. Cleopatra had a child with Caesar and–after his murder–three more with
his protégé. Already she was the wealthiest ruler in the Mediterranean; the
relationship with Antony confirmed her status as the most influential woman of
the age. The two would together attempt to forge a new empire, in an alliance
that spelled their ends. Cleopatra has lodged herself in our imaginations ever
since.

Famous long before she was notorious, Cleopatra has gone down in history for
all the wrong reasons. Shakespeare and Shaw put words in her mouth. Michelangelo
, Tiepolo, and Elizabeth Taylor put a face to her name. Along the way,
Cleopatra’s supple personality and the drama of her circumstances have been
lost. In a masterly return to the classical sources, Stacy Schiff here boldly
separates fact from fiction to rescue the magnetic queen whose death ushered in
a new world order. Rich in detail, epic in scope, Schiff ‘s is a luminous,
deeply original reconstruction of a dazzling life.''',
     '''Parting the Waters by Taylor Branch: (rating:4.34)
First of a 3-volume social history, Parting the Waters is more than a biography
of the Rev. Martin Luther King Jr. during the decade preceding his emergence
as a national figure. This 1000-page effort, which won the Pulitzer Prize as
well as the National Book Critics Circle Award for General Nonfiction, profiles
the key players & events that helped shape the American social landscape
following WWII but before the civil-rights movement of the 60s reached its
climax. Branch then goes a step further, endeavoring to explain how the
struggles evolved as they did by probing the influences of the main actors
while discussing the manner in which events conspired to create fertile ground
for change. Also analyzing the beginnings of black self-consciousness, this
book maps the structure of segregation & bigotry in America between '54 & '63.
The author considers the constantly changing behavior of those in Washington
with regard to the injustice of offical racism operating in many states at this
time.''']


a=True
while a:
    li1c=li1
    li2c=li2
    li3c=li3
    li4c=li4
    li5c=li5
    li6c=li6
    gen=input("\nEnter number corresponding to genre: ")   #Line 9
    if gen=='1':
        if len(li1c)==0:
            print("\nEnd of suggestions")
            continue
        x=random.randint(0,(len(li1c)-1))      
        print('\n',li1c[x])
        li1c.pop(x)      
        
    elif gen=='2':
        if len(li2c)==0:
            print("\nEnd of suggestions")
            continue
        x=random.randint(0,(len(li2c)-1))
        print('\n',li2c[x])
        li2c.pop(x)
        
    elif gen=='3':
        if len(li3c)==0:
            print("\nEnd of suggestions")
            continue
        x=random.randint(0,(len(li3c)-1))
        print('\n',li3c[x])
        li3c.pop(x)
        
    elif gen=='4':
        if len(li4c)==0:
            print("\nEnd of suggestions")
            continue
        x=random.randint(0,(len(li4c)-1))
        print('\n',li4c[x])
        li4c.pop(x)
        
    elif gen=='5':
        if len(li5c)==0:
            print("\nEnd of suggestions")
            continue
        x=random.randint(0,(len(li5c)-1))
        print('\n',li5c[x])
        li5c.pop(x)
        
    elif gen=='6':
        if len(li6c)==0:
            print("\nEnd of suggestions")
            continue
        x=random.randint(0,(len(li6c)-1))
        print('\n',li6c[x])
        li6c.pop(x)

    else:
        print("\nInvalid input")

    ans=input("\nEnter N for exiting the program else enter any other key: ") 
    # Line 10
    if ans.lower()=="n":
        print("\nThank You for using Likeread \n","Have a Good Day!!")
        a=False
        


    
