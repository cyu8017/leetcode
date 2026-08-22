// LeetCode 3715 - Sum of Perfect Square Ancestors
// https://leetcode.com/problems/sum-of-perfect-square-ancestors/

#include <stdlib.h>
#include <string.h>

static int kernel(int x) {
    int res = 1;
    for (int p = 2; p * p <= x; p++) {
        int cnt = 0;
        while (x % p == 0) { x /= p; cnt++; }
        if (cnt % 2 == 1) res *= p;
    }
    if (x > 1) res *= x;
    return res;
}

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

static int** graph;
static int* gn;
static int* ks;
static long long ans;

static void dfs(int u, int p) {
    ans += *mp(ks[u]);
    (*mp(ks[u]))++;
    for (int i = 0; i < gn[u]; i++) {
        int v = graph[u][i];
        if (v != p) dfs(v, u);
    }
    (*mp(ks[u]))--;
}

long long sumOfAncestors(int n, int** edges, int edgesSize, int* edgesColSize, int* nums, int numsSize) {
    (void)edgesColSize; (void)numsSize;
    graph = (int**)calloc((size_t)n, sizeof(int*));
    gn = (int*)calloc((size_t)n, sizeof(int));
    int* gcap = (int*)calloc((size_t)n, sizeof(int));
    for (int i = 0; i < edgesSize; i++) {
        int u = edges[i][0], v = edges[i][1];
        if (gn[u] == gcap[u]) { gcap[u] = gcap[u] ? gcap[u]*2 : 2; graph[u]=(int*)realloc(graph[u],(size_t)gcap[u]*sizeof(int)); }
        if (gn[v] == gcap[v]) { gcap[v] = gcap[v] ? gcap[v]*2 : 2; graph[v]=(int*)realloc(graph[v],(size_t)gcap[v]*sizeof(int)); }
        graph[u][gn[u]++] = v;
        graph[v][gn[v]++] = u;
    }
    ks = (int*)malloc((size_t)n * sizeof(int));
    for (int i = 0; i < n; i++) ks[i] = kernel(nums[i]);
    mc();
    ans = 0;
    dfs(0, -1);
    for (int i = 0; i < n; i++) free(graph[i]);
    free(graph); free(gn); free(gcap); free(ks);
    return ans;
}
