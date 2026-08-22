// LeetCode 3655 - XOR After Range Multiplication Queries II
// https://leetcode.com/problems/xor-after-range-multiplication-queries-ii/

#include <stdlib.h>
int xorAfterQueries(int* nums, int numsSize, int** queries, int queriesSize, int* queriesColSize) {
    (void)queriesColSize;
    const int MOD=1000000007; int n=numsSize;
    int* res=(int*)malloc((size_t)n*sizeof(int)); for(int i=0;i<n;i++) res[i]=nums[i];
    /* group by k */
    typedef struct { int k; int* ups; int n,cap; } GK;
    GK* by=(GK*)NULL; int bn=0,bcap=0;
    for(int qi=0;qi<queriesSize;qi++){
        int l=queries[qi][0],r=queries[qi][1],k=queries[qi][2],v=queries[qi][3], bi=-1;
        for(int t=0;t<bn;t++) if(by[t].k==k){bi=t;break;}
        if(bi<0){ if(bn==bcap){bcap=bcap?bcap*2:8; by=realloc(by,(size_t)bcap*sizeof(GK));} by[bn]=(GK){k,NULL,0,0}; bi=bn++; }
        if(by[bi].n+4>by[bi].cap){ by[bi].cap=by[bi].cap?by[bi].cap*2:16; by[bi].ups=realloc(by[bi].ups,(size_t)by[bi].cap*sizeof(int)); }
        by[bi].ups[by[bi].n++]=l; by[bi].ups[by[bi].n++]=r; by[bi].ups[by[bi].n++]=k; by[bi].ups[by[bi].n++]=v;
    }
    for(int bi=0;bi<bn;bi++){
        int* fac=(int*)malloc((size_t)n*sizeof(int)); for(int i=0;i<n;i++) fac[i]=1;
        for(int t=0;t<by[bi].n;t+=4){ int l=by[bi].ups[t],r=by[bi].ups[t+1],k=by[bi].ups[t+2],v=by[bi].ups[t+3];
            for(int i=l;i<=r;i+=k) fac[i]=(int)((long long)fac[i]*v%MOD); }
        for(int i=0;i<n;i++) res[i]=(int)((long long)res[i]*fac[i]%MOD);
        free(fac); free(by[bi].ups);
    }
    free(by);
    int ans=0; for(int i=0;i<n;i++) ans^=res[i]; free(res); return ans;
}
