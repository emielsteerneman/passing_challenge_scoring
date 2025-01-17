# Pass challenge scoring system

The number of passes made per team does not accurately reflect a team its performance, since one team could face either two very strong or very weak opponents. An example of this can be found in the code. The total number of passes made per team should therefore not be used as a final ranking. This scoring system attempts to solve the problem of last years passing challenge. 

# The Big Picture

Imagine all teams placed in a circle. Whenever two teams play a match, we connect them with an imaginary “spring.” The more one team outscored the other, the more that spring is stretched or compressed. The code then “relaxes” these springs until everyone settles into a position that reflects how strongly they beat or lost to each other over the whole tournament.

# Step-by-Step Explanation

### Start with each team’s total goals
We look at all the goals each team scored in the tournament. That’s our starting point. Think of it like a “guess” at who’s better or worse, based purely on total goals made.

### Connect teams that played each other with an imaginary spring
- If Team A won by a large margin against Team B, the spring between them is “stretched.” It tries to push A “further” ahead and pull B “further” behind.
- If the match was very close, the spring is only slightly stretched or almost relaxed.
- If Team B outscored Team A, then the spring pulls B forward and pushes A back accordingly.

### Arrange teams in a circle and let the springs do their work
We place all teams in a circle: each team is only directly connected to its “neighbors” by these springs. The stretch or compression in each spring is based on the score difference from their match.

### Repeatedly “relax” the springs
The computer acts like a big “physics simulator.” Over many small steps, it adjusts each team’s position (or new “score”) so that everyone moves closer to where the springs want them to be.
- If a spring is stretched too much, it pulls the teams toward each other.
- If a spring is too compressed, it pushes the teams apart.

### Stop when nothing is really changing anymore
After many rounds, the teams settle in positions where no spring is overstretched or over-compressed. That final position gives each team’s adjusted score.

### Use these adjusted scores for the final ranking
Teams with higher adjusted scores are ranked higher. This ranking tries to capture not just how many goals each team scored in total, but also how they performed relative to the specific opponents they faced.

# Why Do This?

Simple total goals can be misleading, because you might have scored a ton of goals against a weaker opponent but still lost to several others.
By using these imaginary springs (one for each match), we get a balance of all the matches. If you beat a strong team (who itself beat others), you tend to get pushed up. If you lose to a weak team, it pushes you down more than just the raw goals suggest.

# The Key Takeaway

Think of it like a tug-of-war network:

- Each match is a rope (a “spring”) connecting the two teams who played.
- The stronger your relative score in a match, the harder that rope pulls you upward in the ranking (and pulls the other team down).
- After letting all ropes pull at once and adjusting teams step by step, everyone lands in a stable place, giving us the final order.