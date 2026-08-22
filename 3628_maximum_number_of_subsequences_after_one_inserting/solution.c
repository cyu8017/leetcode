// LeetCode 3628 - Maximum Number of Subsequences After One Inserting
// https://leetcode.com/problems/maximum-number-of-subsequences-after-one-inserting/

#include <string.h>
static long long llmax(long long a,long long b){return a>b?a:b;}
static long long calc(char* s, char a, char b){ long long cnt=0,aa=0; for(int i=0;s[i];i++){ if(s[i]==b) cnt+=aa; if(s[i]==a) aa++; } return cnt; }
long long numOfSubsequences(char* s) {
    long long l=0,r=0; for(int i=0;s[i];i++) if(s[i]=='T') r++;
    long long ans=0, mx=0;
    for(int i=0;s[i];i++){
        if(s[i]=='T') r--;
        if(s[i]=='C') ans+=l*r;
        if(s[i]=='L') l++;
        mx=llmax(mx,l*r);
    }
    mx=llmax(mx, llmax(calc(s,'L','C'), calc(s,'C','T')));
    return ans+mx;
}
