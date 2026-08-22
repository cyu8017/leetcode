// LeetCode 3585 - Find Weighted Median Node in Tree
// https://leetcode.com/problems/find-weighted-median-node-in-tree/

#include <stdlib.h>
#include <string.h>
int* findMedian(int n, int** edges, int edgesSize, int* edgesColSize, int** queries, int queriesSize, int* queriesColSize, int* returnSize) {
    (void)edgesColSize;(void)queriesColSize;
    typedef struct { int to,w; } E;
    E** g=(E**)calloc((size_t)n,sizeof(E*)); int* gs=(int*)calloc((size_t)n,sizeof(int)); int* gc=(int*)calloc((size_t)n,sizeof(int));
    for(int i=0;i<edgesSize;i++){
        int u=edges[i][0],v=edges[i][1],w=edges[i][2];
        for(int r=0;r<2;r++){ int a=r?v:u,b=r?u:v;
            if(gs[a]==gc[a]){ gc[a]=gc[a]?gc[a]*2:4; g[a]=realloc(g[a],(size_t)gc[a]*sizeof(E)); }
            g[a][gs[a]++] = (E){b,w};
        }
    }
    int* ans=(int*)malloc((size_t)queriesSize*sizeof(int));
    for(int qi=0;qi<queriesSize;qi++){
        int u=queries[qi][0], v=queries[qi][1];
        int* parent=(int*)malloc((size_t)n*sizeof(int));
        int* pw=(int*)calloc((size_t)n,sizeof(int));
        for(int i=0;i<n;i++) parent[i]=-2; parent[u]=-1;
        int* q=(int*)malloc((size_t)n*sizeof(int)); int qh=0,qt=0; q[qt++]=u;
        while(qh<qt){ int x=q[qh++]; if(x==v) break;
            for(int i=0;i<gs[x];i++){ int to=g[x][i].to; if(parent[to]==-2){ parent[to]=x; pw[to]=g[x][i].w; q[qt++]=to; } }
        }
        int* nodes=(int*)malloc((size_t)n*sizeof(int)); int* weights=(int*)malloc((size_t)n*sizeof(int));
        int nn=0, wn=0; int cur=v; nodes[nn++]=v;
        while(cur!=u){ weights[wn++]=pw[cur]; cur=parent[cur]; nodes[nn++]=cur; }
        for(int i=0,j=nn-1;i<j;i++,j--){ int t=nodes[i]; nodes[i]=nodes[j]; nodes[j]=t; }
        for(int i=0,j=wn-1;i<j;i++,j--){ int t=weights[i]; weights[i]=weights[j]; weights[j]=t; }
        int total=0; for(int i=0;i<wn;i++) total+=weights[i];
        int need=(total+1)/2, sum=0, med=u;
        for(int i=0;i<wn;i++){ sum+=weights[i]; med=nodes[i+1]; if(sum>=need) break; }
        ans[qi]=med;
        free(parent);free(pw);free(q);free(nodes);free(weights);
    }
    for(int i=0;i<n;i++) free(g[i]); free(g);free(gs);free(gc);
    *returnSize=queriesSize; return ans;
}
