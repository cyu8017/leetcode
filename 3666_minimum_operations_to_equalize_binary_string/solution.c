// LeetCode 3666 - Minimum Operations to Equalize Binary String
// https://leetcode.com/problems/minimum-operations-to-equalize-binary-string/

#include <stdlib.h>
#include <string.h>
#include <stdbool.h>
static int imin(int a,int b){return a<b?a:b;}
static int imax(int a,int b){return a>b?a:b;}
/* BFS on count of zeros; sets of reachable counts by parity via bool arrays */
int minOperations(char* s, int k) {
    int n=(int)strlen(s);
    bool* alive[2]; alive[0]=(bool*)calloc((size_t)n+1,sizeof(bool)); alive[1]=(bool*)calloc((size_t)n+1,sizeof(bool));
    for(int i=0;i<=n;i++) alive[i%2][i]=true;
    int cnt0=0; for(int i=0;s[i];i++) if(s[i]=='0') cnt0++;
    alive[cnt0%2][cnt0]=false;
    int* q=(int*)malloc((size_t)(n+2)*sizeof(int)); int qh=0,qt=0; q[qt++]=cnt0; int ans=0;
    while(qh<qt){
        int sz=qt-qh; int* nq=(int*)malloc((size_t)(n+2)*sizeof(int)); int nqn=0;
        for(int s0=0;s0<sz;s0++){
            int cur=q[qh++]; if(cur==0){ free(q); free(nq); free(alive[0]); free(alive[1]); return ans; }
            int l=cur+k-2*imin(cur,k), r=cur+k-2*imax(k-n+cur,0);
            bool* t=alive[l%2];
            for(int val=l; val<=r; val+=2) if(val>=0&&val<=n&&t[val]){ t[val]=false; nq[nqn++]=val; }
        }
        free(q); q=nq; qh=0; qt=nqn; ans++;
    }
    free(q); free(alive[0]); free(alive[1]); return -1;
}
