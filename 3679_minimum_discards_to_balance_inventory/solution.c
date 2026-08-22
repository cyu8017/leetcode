// LeetCode 3679 - Minimum Discards to Balance Inventory
// https://leetcode.com/problems/minimum-discards-to-balance-inventory/

#include <stdlib.h>
#include <string.h>

#define MAP_SIZE 200003
static int mk[MAP_SIZE], mv[MAP_SIZE];
static char mu[MAP_SIZE];
static void mc(void){memset(mu,0,sizeof(mu));}
static int* mp(int k){
    int i=(int)((unsigned)k%MAP_SIZE);
    while(mu[i]&&mk[i]!=k){if(++i==MAP_SIZE)i=0;}
    if(!mu[i]){mu[i]=1;mk[i]=k;mv[i]=0;}
    return &mv[i];
}

int minArrivalsToDiscard(int* arrivals, int arrivalsSize, int w, int m) {
    mc();
    int n = arrivalsSize;
    int* marked = (int*)calloc((size_t)n, sizeof(int));
    int ans = 0;
    for (int i = 0; i < n; i++) {
        int x = arrivals[i];
        if (i >= w) {
            *mp(arrivals[i - w]) -= marked[i - w];
        }
        if (*mp(x) >= m) {
            ans++;
        } else {
            marked[i] = 1;
            (*mp(x))++;
        }
    }
    free(marked);
    return ans;
}
