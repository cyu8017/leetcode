// LeetCode 3604 - Minimum Time to Reach Destination in Directed Graph
// https://leetcode.com/problems/minimum-time-to-reach-destination-in-directed-graph/

#include <stdlib.h>
#include <limits.h>
typedef struct { int to,start,end; } Edge;
typedef struct { int u,t; } Item;
static void heap_push(Item* h, int* hn, Item x){ int i=(*hn)++; h[i]=x; while(i){ int p=(i-1)/2; if(h[p].t<=h[i].t) break; Item t=h[p]; h[p]=h[i]; h[i]=t; i=p; } }
static Item heap_pop(Item* h, int* hn){ Item r=h[0]; h[0]=h[--(*hn)]; int i=0; for(;;){ int l=i*2+1,rgt=l+1,sm=i; if(l<*hn&&h[l].t<h[sm].t) sm=l; if(rgt<*hn&&h[rgt].t<h[sm].t) sm=rgt; if(sm==i) break; Item t=h[i]; h[i]=h[sm]; h[sm]=t; i=sm; } return r; }
int minTime(int n, int** edges, int edgesSize, int* edgesColSize) {
    (void)edgesColSize;
    Edge** g=(Edge**)calloc((size_t)n,sizeof(Edge*)); int* gs=(int*)calloc((size_t)n,sizeof(int)); int* gc=(int*)calloc((size_t)n,sizeof(int));
    for(int i=0;i<edgesSize;i++){
        int u=edges[i][0],v=edges[i][1],s=edges[i][2],en=edges[i][3];
        if(gs[u]==gc[u]){ gc[u]=gc[u]?gc[u]*2:4; g[u]=realloc(g[u],(size_t)gc[u]*sizeof(Edge)); }
        g[u][gs[u]++]=(Edge){v,s,en};
    }
    const int inf=INT_MAX/4;
    int* dist=(int*)malloc((size_t)n*sizeof(int)); for(int i=0;i<n;i++) dist[i]=inf; dist[0]=0;
    Item* h=(Item*)malloc((size_t)(edgesSize*2+n+5)*sizeof(Item)); int hn=0;
    heap_push(h,&hn,(Item){0,0});
    while(hn){
        Item cur=heap_pop(h,&hn);
        if(cur.t!=dist[cur.u]) continue;
        if(cur.u==n-1){ for(int i=0;i<n;i++) free(g[i]); free(g);free(gs);free(gc);free(dist);free(h); return cur.t; }
        for(int i=0;i<gs[cur.u];i++){
            Edge e=g[cur.u][i]; int t=cur.t; if(t>e.end) continue; if(t<e.start) t=e.start; int nt=t+1;
            if(nt<dist[e.to]){ dist[e.to]=nt; heap_push(h,&hn,(Item){e.to,nt}); }
        }
    }
    int ans=dist[n-1]==inf?-1:dist[n-1];
    for(int i=0;i<n;i++) free(g[i]); free(g);free(gs);free(gc);free(dist);free(h);
    return ans;
}
