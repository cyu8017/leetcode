// LeetCode 3593 - Minimum Increments to Equalize Leaf Paths
// https://leetcode.com/problems/minimum-increments-to-equalize-leaf-paths/

#include <stdlib.h>
static int g_ans;
static int** graph; static int* gSize; static int* cost_g;
static long long dfs(int u, int p){
    int childN=0; long long* childVals=malloc((size_t)gSize[u]*sizeof(long long));
    for(int i=0;i<gSize[u];i++){
        int v=graph[u][i]; if(v==p) continue;
        childVals[childN++]=dfs(v,u);
    }
    if(childN==0){ free(childVals); return cost_g[u]; }
    long long mx=0; for(int i=0;i<childN;i++) if(childVals[i]>mx) mx=childVals[i];
    for(int i=0;i<childN;i++) if(childVals[i]<mx) g_ans++;
    free(childVals); return mx+cost_g[u];
}
int minIncrease(int n, int** edges, int edgesSize, int* edgesColSize, int* cost, int costSize) {
    (void)edgesColSize;(void)costSize;
    graph=(int**)calloc((size_t)n,sizeof(int*)); gSize=(int*)calloc((size_t)n,sizeof(int));
    int* gCap=(int*)calloc((size_t)n,sizeof(int));
    for(int i=0;i<edgesSize;i++){
        int u=edges[i][0],v=edges[i][1];
        for(int r=0;r<2;r++){ int a=r?v:u,b=r?u:v;
            if(gSize[a]==gCap[a]){ gCap[a]=gCap[a]?gCap[a]*2:4; graph[a]=realloc(graph[a],(size_t)gCap[a]*sizeof(int)); }
            graph[a][gSize[a]++]=b;
        }
    }
    cost_g=cost; g_ans=0; dfs(0,-1);
    for(int i=0;i<n;i++) free(graph[i]); free(graph); free(gSize); free(gCap);
    return g_ans;
}
