class Solution:
    def numTeams(self, rating):
        ans=0
        for j,x in enumerate(rating):
            ll=sum(y<x for y in rating[:j]);lg=j-ll
            rg=sum(y>x for y in rating[j+1:]);rl=len(rating)-j-1-rg
            ans+=ll*rg+lg*rl
        return ans
