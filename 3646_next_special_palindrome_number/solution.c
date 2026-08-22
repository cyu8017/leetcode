// LeetCode 3646 - Next Special Palindrome Number
// https://leetcode.com/problems/next-special-palindrome-number/

#include <stdlib.h>
#include <stdio.h>
#include <string.h>
static long long* cands; static int cn, ccap;
static int halfCnt[10], mid, halfLen;
static void add_cand(long long v){ if(cn==ccap){ccap=ccap?ccap*2:64; cands=realloc(cands,(size_t)ccap*sizeof(long long));} cands[cn++]=v; }
static void dfs(int pos, int* cur){
    if(pos==halfLen){
        char s[40]; int len=0;
        for(int i=0;i<halfLen;i++) s[len++]=(char)('0'+cur[i]);
        if(mid>0) s[len++]=(char)('0'+mid);
        for(int i=halfLen-1;i>=0;i--) s[len++]=(char)('0'+cur[i]);
        s[len]=0; long long val=0; sscanf(s,"%lld",&val); add_cand(val); return;
    }
    for(int d=1;d<=9;d++) if(halfCnt[d]){ halfCnt[d]--; cur[pos]=d; dfs(pos+1,cur); halfCnt[d]++; }
}
static void gen(int mask){
    int total=0,odd=0;
    for(int d=1;d<=9;d++) if(mask>>d&1){ total+=d; if(d%2) odd++; }
    if(total==0||total>18||odd>1) return;
    memset(halfCnt,0,sizeof(halfCnt)); mid=0;
    for(int d=1;d<=9;d++){ if(!(mask>>d&1)) continue; halfCnt[d]=d/2; if(d%2) mid=d; }
    halfLen=total/2; int cur[20]; dfs(0,cur);
}
static int cmp_ll(const void*a,const void*b){ long long x=*(const long long*)a,y=*(const long long*)b; return x<y?-1:x>y; }
long long specialPalindrome(long long n) {
    cands=NULL; cn=ccap=0;
    for(int mask=1;mask<(1<<10);mask++){ if(mask&1) continue; gen(mask); }
    qsort(cands,(size_t)cn,sizeof(long long),cmp_ll);
    long long ans=-1; for(int i=0;i<cn;i++) if(cands[i]>n){ ans=cands[i]; break; }
    free(cands); return ans;
}
