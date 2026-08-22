// LeetCode 3629 - Minimum Jumps to Reach End via Prime Teleportation
// https://leetcode.com/problems/minimum-jumps-to-reach-end-via-prime-teleportation/

#include <stdlib.h>
#include <stdbool.h>
#include <string.h>
#define MX 1000001
static int* factors[MX]; static int fsz[MX]; static int finited;
static void ensure_factors(void){
    if(finited) return; finited=1;
    for(int i=2;i<MX;i++) if(fsz[i]==0) for(int j=i;j<MX;j+=i){ factors[j]=realloc(factors[j],(size_t)(fsz[j]+1)*sizeof(int)); factors[j][fsz[j]++]=i; }
}
int minJumps(int* nums, int numsSize) {
    ensure_factors();
    int n=numsSize;
    /* map prime -> indices list; use array of dynamic for primes appearing */
    typedef struct { int key; int* ids; int n,cap; } Bucket;
    Bucket* bucks=NULL; int bn=0,bcap=0;
    #define FIND(p,out) do{ out=-1; for(int _i=0;_i<bn;_i++) if(bucks[_i].key==(p)){out=_i;break;} }while(0)
    for(int i=0;i<n;i++){
        int x=nums[i];
        for(int t=0;t<fsz[x];t++){
            int p=factors[x][t], bi; FIND(p,bi);
            if(bi<0){ if(bn==bcap){bcap=bcap?bcap*2:16; bucks=realloc(bucks,(size_t)bcap*sizeof(Bucket));} bucks[bn]=(Bucket){p,NULL,0,0}; bi=bn++; }
            if(bucks[bi].n==bucks[bi].cap){ bucks[bi].cap=bucks[bi].cap?bucks[bi].cap*2:4; bucks[bi].ids=realloc(bucks[bi].ids,(size_t)bucks[bi].cap*sizeof(int)); }
            bucks[bi].ids[bucks[bi].n++]=i;
        }
    }
    bool* vis=(bool*)calloc((size_t)n,sizeof(bool)); vis[0]=true;
    int* q=(int*)malloc((size_t)n*sizeof(int)); int qh=0,qt=0; q[qt++]=0; int ans=0;
    while(qh<qt){
        int sz=qt-qh;
        for(int s=0;s<sz;s++){
            int i=q[qh++]; if(i==n-1){ for(int t=0;t<bn;t++) free(bucks[t].ids); free(bucks); free(vis); free(q); return ans; }
            int bi; FIND(nums[i],bi);
            int idxcap= (bi>=0?bucks[bi].n:0)+2; int* idx=malloc((size_t)idxcap*sizeof(int)); int in=0;
            if(bi>=0){ for(int t=0;t<bucks[bi].n;t++) idx[in++]=bucks[bi].ids[t]; bucks[bi].n=0; }
            idx[in++]=i+1; if(i>0) idx[in++]=i-1;
            for(int t=0;t<in;t++){ int j=idx[t]; if(j>=0&&j<n&&!vis[j]){ vis[j]=true; q[qt++]=j; } }
            free(idx);
        }
        ans++;
    }
    for(int t=0;t<bn;t++) free(bucks[t].ids); free(bucks); free(vis); free(q); return -1;
}
