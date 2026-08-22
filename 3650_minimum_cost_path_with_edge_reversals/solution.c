// LeetCode 3650 - Minimum Cost Path with Edge Reversals
// https://leetcode.com/problems/minimum-cost-path-with-edge-reversals/

#include <stdlib.h>
#include <limits.h>
typedef struct { int v,w; } E;
typedef struct { int x,i; } P;
static void hpush(P* h,int* hn,P x){ int i=(*hn)++; h[i]=x; while(i){int p=(i-1)/2; if(h[p].x<=h[i].x)break; P t=h[p];h[p]=h[i];h[i]=t;i=p;} }
static P hpop(P* h,int* hn){ P r=h[0]; h[0]=h[--(*hn)]; int i=0; for(;;){int l=i*2+1,rg=l+1,sm=i; if(l<*hn&&h[l].x<h[sm].x)sm=l; if(rg<*hn&&h[rg].x<h[sm].x)sm=rg; if(sm==i)break; P t=h[i];h[i]=h[sm];h[sm]=t;i=sm;} return r; }
int minCost(int n, int** edges, int edgesSize, int* edgesColSize) {
    (void)edgesColSize;
    E** g=(E**)calloc((size_t)n,sizeof(E*)); int* gs=(int*)calloc((size_t)n,sizeof(int)); int* gc=(int*)calloc((size_t)n,sizeof(int));
    for(int i=0;i<edgesSize;i++){
        int u=edges[i][0],v=edges[i][1],w=edges[i][2];
        if(gs[u]==gc[u]){gc[u]=gc[u]?gc[u]*2:4;g[u]=realloc(g[u],(size_t)gc[u]*sizeof(E));} g[u][gs[u]++]=(E){v,w};
        if(gs[v]==gc[v]){gc[v]=gc[v]?gc[v]*2:4;g[v]=realloc(g[v],(size_t)gc[v]*sizeof(E));} g[v][gs[v]++]=(E){u,w*2};
    }
    int inf=INT_MAX/4; int* dist=(int*)malloc((size_t)n*sizeof(int)); for(int i=0;i<n;i++) dist[i]=inf; dist[0]=0;
    P* h=(P*)malloc((size_t)(edgesSize*4+n)*sizeof(P)); int hn=0; hpush(h,&hn,(P){0,0});
    while(hn){
        P cur=hpop(h,&hn); if(cur.x>dist[cur.i]) continue; if(cur.i==n-1){ int ans=cur.x; for(int i=0;i<n;i++)free(g[i]); free(g);free(gs);free(gc);free(dist);free(h); return ans; }
        for(int t=0;t<gs[cur.i];t++){ int v=g[cur.i][t].v,w=g[cur.i][t].w; int nd=cur.x+w; if(nd<dist[v]){ dist[v]=nd; hpush(h,&hn,(P){nd,v}); } }
    }
    for(int i=0;i<n;i++)free(g[i]); free(g);free(gs);free(gc);free(dist);free(h); return -1;
}
