import random as rand

subjects= """Champ,
Fact:
Everybody says
Dang
Check it:
Just saying...
Superstar,
Tiger,
Self,
Know this:
News alert:
Friend,
Ace,
Excuse me but
Experts agree:
In my opinion,
Hear ye, hear ye:
Okay, listen up:
"""

subject_descriptors="""the mere idea of you
your soul
your hair today
everything you do
your personal style
every thought you have
that sparkle in your eye
your presence here
what you got going on
the essential you
your life's journey
that saucy personality
your DNA
that brain of yours
your choice of attire
the way you roll
whatever your secret is
all of y'all
"""


predicates = """has serious game,
rains magic,
deserves the Nobel Prize,
raises the roof,
breeds miracles,
is paying off big time,
shows mad skills,
just shimmers,
is a national treasure,
gets the party hopping,
is the next big thing.
roars like a lion,
is a rainbow factory,
is made of diamonds,
makes birds sing.
should be taught in school,
makes my world go 'round
is 100 percent legit,
"""

predicate_descriptors="""24/7.
can I get an amen?
and that's a fact.
so treat yourself.
you feel me?
that's just science.
would I lie?
for reals.
mic drop.
you hidden gem.
snuggle bear.
period.
can I get an amen?
now let's dance.
high five.
say it again!
according to any credible news source.
so get used to it.
"""

subject_list=subjects.splitlines()
sub_descriptor_list=subject_descriptors.splitlines()
predicates_list=predicates.splitlines()
pred_descriptor_list=  predicate_descriptors.splitlines()


def pep_talk_generation():
        pep_talk = subject_list[rand.randint(0,17)] +" "+ sub_descriptor_list[rand.randint(0,17)] +" "+ predicates_list[rand.randint(0,17)] +" "+ pred_descriptor_list[rand.randint(0,17)]
        print(pep_talk)
        return pep_talk
