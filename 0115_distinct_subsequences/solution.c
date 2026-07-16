// LeetCode 0115 - Distinct Subsequences
#include <stdlib.h>
#include <string.h>
int numDistinct(char* s, char* t) {
    int n=strlen(t); unsigned long long *dp=calloc(n+1,sizeof(*dp)); dp[0]=1;
    for(int i=0;s[i];i++) for(int j=n;j>0;j--) if(s[i]==t[j-1]) dp[j]+=dp[j-1];
    int ans=(int)dp[n]; free(dp); return ans;
}