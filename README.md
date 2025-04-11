## The current situation. More passes = better ranking
In the 2024 tournament, the ranking of the passing challenge was calculated by counting up the total number of passes each team had made. The team with the most passes received 1st place, the team with the second most passes 2nd place, and so on. 

## The issue with this system
Let's pick two strong teams, ZJUNLict and TIGERs Mannheim. What if these are your two opponents for the passing challenge? It's definitely going to be difficult. Yet, your team persists and you make 2 passes against ZJUNLict (they make 5), and 4 passes against TIGERs (they make 1). Your total number of passes is now 2 + 4 = 6. That's not a lot, but what do you expect against two top-tier teams. 

Now, let's also take two low-tier Div B teams, and another team, RoboTeam Twente. RoboTeam Twente plays quite well against these two teams, making 4 + 7 = 11 passes. RoboTeam Twente made more passes than your team, so they have a higher ranking. But that doesn't seem really fair does it? You had to play against two top-tier Div-A teams, and RoboTeam Twente against two low-tier Div B teams! 

Just looking at the total number of passes made doesn't work. So, how do we right this wrong? We somehow have to take into account that one team might just have two very strong opponents, while another might have two weak opponents. Having even more matches to have your team play against RoboTeam Twente isn't an option, so ..?

## An exaggerated example
If you pass as well as another team (meaning, an almost equal number of passes in a match), it makes sense that you and the other team have around the same ranking. If you destroy another team, your team should have a much higher ranking than that other team. Therefore, let's start with an exaggerated example tournament.

Team 1 | Passes | Team 2
---: | :---: | :--- 
ZJUNLict | 5 - 2 | ER-Force
ER-Force | 4 - 1 | TIGERs
TIGERs | 45 - 3 | Team X
Team X | 8 - 11 | Team Y
Team Y | 12 - 50 | ZJUNLict

This brings the total number of passes for each team to the following:

Team | Passes | Ranking
---: | --- | ---
ZJUNLict    | 55 | 1st
TIGERs      | 46 | 2nd
Team Y | 23 | 3rd
Team X        | 11 | 4th
ER-Force    |  6 | 5th
 
This ranking doesn't make much sense. ER-Force played so well against ZJUNLict and even beat TIGERs. Yet, it's placed last? The problem here is that ER-Force had two strong opponents, while ZJUNLict and TIGERs both also had one relative weak opponent.  

## Let's try ranking by relative score
Let's start by putting ER-Force at a score of 0. This score is relative to the scores of other teams, so 0 doesn't say anything yet. ER-Force had 3 more passes in it's match against TIGERs, so let's place TIGER's at -3. Team X, because of its -42 pass difference against TIGERs will move to -3 - 42 = -45. Team Y will move to -45 + 3 = -42. ZJUNLict will move to -42 + 38 = -4. Now let's look  at the score again.

Team | Score | Ranking
---: | --- | ---
ER-Force    |  0 | 1st
TIGERs      | -3 | 2nd
ZJUNLict    | -4 | 3rd
Team Y      | -42 | 4th
Team X      | -45 | 5th

This makes a bit more sense. ER-Force ends up above TIGERs, which it won against. It also placed above ZJUNLict, against which it lost. That still feels a bit weird.. **But wait**. If we continue the scoring system, given that ZJUNLict had 3 passes more against ER-Force, ER-Force should end up at the score -4 - 3 = -7 !? But ER-Force already received the score of 0 all the way at the beginning.. What now? Does ER-Force receive a score of 0 or -7? If we give ER-Force the score of 0, it stays on the 1st place. If we give it the score of -7, it receives 3rd place. But then, at -7, shouldn't TIGERs also move down again to -7 - 3 = -10? Maybe we should give ER-Force a score of -3.5, in the middle. But then again, TIGERs would have to move down to -6.5? Maybe TIGERs its score should then be averaged as well? And because TIGERs moves down, Team X moves down again as well. As you can see, this is an infinite circle, where we keep pushing the score of teams up and down. Fortunately, there is a solution to this seemingly infinite process. 

## Ending this never-ending circle
What we can say from the previous example, is that ER-Force is "pushing down" TIGERs with a "force" of 3 (since it made 3 more passes than TIGERs in their match). ER-Force is also pushing ZJUNLict up, with a force of 3 (since it made 3 passes less than ZJUNLict in their match). This is the same as saying that ZJUNLict is pushing ER-Force down with a force of 3. Following the example, all teams are exercising forces on other teams they played against. 

To end this confusing tug-of-war, we place all teams in a circle, and we let each team **pull** or **push** the teams it faced, with a force equal to the difference in passes. In other words, if ER-Force is "up" 3 passes against TIGERs, it pushes TIGERs "down" by 3. Meanwhile, if ER-Force is "down" 3 passes against ZJUNLict, ZJUNLict pushes ER-Force "down" by 3.  

Because every team faces exactly two other teams in this simplified ring (one on its left, one on its right), we can write down an equation describing how the forces from each opponent pull or push that team up or down. Then we **iterate** these equations over and over, adjusting each team's score step by step. One iteration might nudge ER-Force slightly lower (due to ZJUNLict) and TIGERs slightly lower again (due to ER-Force), and so on around the circle. Eventually, if we keep doing these tiny nudges, all forces balance out, and we end up with a stable set of scores—no team wants to move up or down anymore, because the total pull and push on each team is zero.

Mathematically, this final solution is where each team's position perfectly balances the net "force" coming from its matches. Intuitively, a team that lost badly to a top contender will get pushed down quite a bit. If it also beat another team by a large margin, it will get pulled back up. And so on. So instead of thinking in a linear chain of who beat whom first and then second, this method captures all of those interactions at once and finds a sweet spot where every match’s pass difference is factored in fairly.

## Closed loop solution
_Hearken, scholars and seekers of knowledge! Let it be known that Jorn de Jong, wise scholar and master of his craft, sworn to the noble house of RoboTeam Twente, hailing from the distant land of Meppel, hath achieved a great and wondrous feat! By wisdom and skill alike, he hath uncovered a closed-form solution for the passing challenge scoring system, casting aside the burdens of iteration! Rejoice, for such a marvel graces our halls this day!_

There is a closed loop solution to the above never-ending cycle. 
