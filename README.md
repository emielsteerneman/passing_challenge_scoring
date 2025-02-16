## The current situation. More passes = better ranking
In the 2024 tournament, the ranking of the passing challenge was calculated by counting up the total number of passes each team had made. The team with the most passes received 1st place, the team with the second most passes 2nd place, and so on. 

## The issue with this system
Let's pick two strong teams, ZJUNLict and TIGERs Mannheim. What if these are your two opponents for the passing challenge? It's definitely going to be difficult. Yet, your team persists and you make 2 passes against ZJUNLict (they make 5), and 4 passes against TIGERs (they make 1). Your total number of passes is now 2 + 4 = 6. That's not a lot, but what do you expect against two top-tier teams. 

Now, let's also take two low-tier Div B teams, and another team, RoboTeam Twente. RoboTeam Twente plays quite well against these two teams, making 4 + 7 = 11 passes. RoboTeam Twente made more passes than your team, so they have a higher ranking. But that doesn't seem really fair does it? You had to play against two top-tier Div-A teams, and RoboTeam Twente against two low-tier Div B teams! 

Just looking at the total number of passes made doesn't work. So, how do we wrong this right? We somehow have to take into account that one team might just have two very strong opponents, while another might have two weak opponents. Having even more matches to have your team play against RoboTeam Twente isn't an option, so ..?

## An exaggerated example
If you pass as well as another team (meaning, an almost equal number of passes in a match), it makes sense that you and the other team have around the same ranking. If you destroy another team, your team should have a much higher ranking than that other team. Therefore, let's start with an exaggerated example tournament.

Team 1 | Passes | Team 2
---: | :---: | :--- 
ZJUNLict | 5 - 2 | ER-Force
ER-Force | 4 - 1 | TIGERs
TIGERs | 45 - 3 | KIKS
KIKS | 8 - 11 | RoboDragons
RoboDragons | 12 - 50 | ZJUNLict

This brings the total number of passes for each team to the following:

Team | Passes | Ranking
---: | --- | ---
ZJUNLict    | 55 | 1st
ER-Force    |  6 | 5th
TIGERs      | 46 | 2nd
KIKS        | 11 | 4th
RoboDragons | 23 | 3rd
 
This ranking doesn't make much sense. ER-Force played so well against ZJUNLict and even beat TIGERs. Yet, it's placed last? The problem here is that ER-Force had two strong opponents, while ZJUNLict and TIGERs both also had one relative weak opponent.  

## Let's try ranking by relative score
Let's start by putting ER-Force at a score of 0. This score is relative to the scores of other teams, so 0 doesn't say anything yet. ER-Force had 3 more passes in it's match against TIGERs, so let's place TIGER's at -3. KIKS, because of its -42 pass difference against TIGERs will move to -3 - 42 = -45. RoboDragons will move to -45 + 3 = -42. ZJUNLict will move to -42 + 38 = -4. Now let's look  at the score again.

Team | Score | Ranking
---: | --- | ---
ZJUNLict    | -4 | 3rd
ER-Force    |  0 | 1st
TIGERs      | -3 | 2nd
KIKS        | -45 | 5th
RoboDragons | -42 | 4th

This makes a bit more sense. ER-Force ends up above TIGERs, which it won against. It also placed above ZJUNLict, against which it lost. That still feels a bit weird.. **But wait**. If we continue the scoring system, given that ZJUNLict had 3 passes more against ER-Force, ER-Force should end up at the score -4 - 3 = -7 !? But ER-Force already received the score of 0 all the way at the beginning.. What now? Does ER-Force receive a score of 0 or -7? If we give ER-Force the score of 0, it stays on the 1st place. If we give it the score of -7, it receives 3rd place. But then, at -7, shouldn't TIGERs also move down again to -7 - 3 = -10? Maybe we should give ER-Force a score of -3.5, in the middle. But then again, TIGERs would have to move down to -6.5? Maybe TIGERs its score should then be averaged as well? And because TIGERs moves down, KIKS moves down again as well. As you can see, this is an infinite circle, where we keep pushing the score of teams up and down. Fortunately, there is a solution to this seemingly infinite process. 






### Start with each team at a score of 0

### Connect teams that played against eachother with an imaginary spring
- If Team A won by a large margin against Team B, the spring between them is stretched. It tries to push A up and B down.
- If the match was very close, the spring pulls team A and team B closer together.

### Arrange teams in a circle and let the springs do their work
We place all teams in a circle: each team is only directly connected to its “neighbors” by these springs. The stretch or compression in each spring is based on the score difference from their match.

### Repeatedly “relax” the springs
The code acts like a physics simulator. Over many small steps, it adjusts each team’s position (or new “score”) so that everyone moves closer to where the springs want them to be.
- If a spring is stretched too much, it pulls the teams toward each other.
- If a spring is compressed too much, it pushes the teams apart.

### Stop when nothing is really changing anymore
After many rounds, the teams settle in positions where no spring is overstretched or over-compressed. That final position gives each team’s adjusted score.

### Use these adjusted scores for the final ranking
Teams with higher adjusted scores are ranked higher. This ranking tries to capture not just how many passes each team scored in total, but also how they performed relative to the specific opponents they faced.

# Why Do This?

Simple total passes can be misleading, because you might have scored a ton of passes against a weaker opponent but still lost to several others.
By using these imaginary springs (one for each match), we get a balance of all the matches. If you beat a strong team (who itself beat others), you tend to get pushed up. If you lose to a weak team, it pushes you down more than just the raw passes suggest.

# The Key Takeaway

Think of it like a tug-of-war network:

- Each match is a rope (a “spring”) connecting the two teams who played.
- The stronger your relative score in a match, the harder that rope pulls you upward in the ranking (and pulls the other team down).
- After letting all ropes pull at once and adjusting teams step by step, everyone lands in a stable place, giving us the final order.