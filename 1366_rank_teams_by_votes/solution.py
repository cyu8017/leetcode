class Solution:
    def rankTeams(self, votes):
        m=len(votes[0]); count={c:[0]*m for c in votes[0]}
        for v in votes:
            for i,c in enumerate(v):count[c][i]+=1
        return ''.join(sorted(count,key=lambda c:(tuple(-x for x in count[c]),c)))
