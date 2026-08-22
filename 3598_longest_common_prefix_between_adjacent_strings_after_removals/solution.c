// LeetCode 3598 - Longest Common Prefix Between Adjacent Strings After Removals
// https://leetcode.com/problems/longest-common-prefix-between-adjacent-strings-after-removals/

#include <stdlib.h>
#include <string.h>
static int imin(int a,int b){return a<b?a:b;}
static int calc(char* s, char* t){ int m=imin((int)strlen(s),(int)strlen(t)); for(int k=0;k<m;k++) if(s[k]!=t[k]) return k; return m; }
/* multiset of LCP lengths */
typedef struct { int key,cnt; } N;
static N* ms; static int msn, mscap;
static void ms_add(int x,int d){
    for(int i=0;i<msn;i++) if(ms[i].key==x){ ms[i].cnt+=d; if(ms[i].cnt==0){ for(int j=i;j<msn-1;j++) ms[j]=ms[j+1]; msn--; } return; }
    if(d<=0) return;
    if(msn==mscap){ mscap=mscap?mscap*2:8; ms=realloc(ms,(size_t)mscap*sizeof(N)); }
    ms[msn++]=(N){x,d};
}
static int ms_max(void){ int mx=0; for(int i=0;i<msn;i++) if(ms[i].key>mx) mx=ms[i].key; return mx; }
int* longestCommonPrefix(char** words, int wordsSize, int* returnSize) {
    int n=wordsSize; msn=0; mscap=0; ms=NULL;
    for(int i=0;i+1<n;i++) ms_add(calc(words[i],words[i+1]),1);
    int* ans=(int*)calloc((size_t)n,sizeof(int));
    for(int i=0;i<n;i++){
        if(i+1<n) ms_add(calc(words[i],words[i+1]),-1);
        if(i-1>=0) ms_add(calc(words[i-1],words[i]),-1);
        if(i-1>=0 && i+1<n) ms_add(calc(words[i-1],words[i+1]),1);
        if(msn>0){ int mx=ms_max(); if(mx>0) ans[i]=mx; }
        if(i-1>=0 && i+1<n) ms_add(calc(words[i-1],words[i+1]),-1);
        if(i-1>=0) ms_add(calc(words[i-1],words[i]),1);
        if(i+1<n) ms_add(calc(words[i],words[i+1]),1);
    }
    free(ms); *returnSize=n; return ans;
}
