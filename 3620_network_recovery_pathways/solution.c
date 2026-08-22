// LeetCode 3620 - Network Recovery Pathways
// https://leetcode.com/problems/network-recovery-pathways/

#include <stdlib.h>
#include <limits.h>
#include <stdbool.h>
typedef struct { int v,w; } E;
typedef struct { int d,u; } Item;
static void hpush(Item* h,int* hn,Item x){ int i=(*hn)++; h[i]=x; while(i){int p=(i-1)/2; if(h[p].d<=h[i].d)break; Item t=h[p];h[p]=h[i];h[i]=t;i=p;} }
static Item hpop(Item* h,int* hn){ Item r=h[0]; h[0]=h[--(*hn)]; int i=0; for(;;){int l=i*2+1,rg=l+1,sm=i; if(l<*hn&&h[l].d<h[sm].d)sm=l; if(rg<*hn&&h[rg].d<h[sm].d)sm=rg; if(sm==i)break; Item t=h[i];h[i]=h[sm];h[sm]=t;i=sm;} return r; }
static E** g; static int* gs; static int n_g; static long long k_g;
static bool check(int mid){
    const int INF=INT_MAX/4; int* dist=(int*)malloc((size_t)n_g*sizeof(int)); for(int i=0;i<n_g;i++) dist[i]=INF; dist[0]=0;
    Item* h=(Item*)malloc((size_t)(n_g*64+8)*sizeof(Item)); int hn=0; hpush(h,&hn,(Item){0,0});
    bool ok=false;
    while(hn){
        Item cur=hpop(h,&hn); int d=cur.d,u=cur.u;
        if((long long)d>k_g){ ok=false; break; }
        if(u==n_g-1){ ok=true; break; }
        if(dist[u]<d) continue;
        for(int i=0;i<gs[u];i++){ int v=g[u][i].v,w=g[u][i].w; if(w<mid) continue; int nd=d+w; if(nd<dist[v]){ dist[v]=nd; hpush(h,&hn,(Item){nd,v}); } }
    }
    free(dist); free(h); return ok;
}
int findMaxPathScore(int** edges, int edgesSize, int* edgesColSize, bool* online, int onlineSize, long long k) {
    (void)edgesColSize; n_g=onlineSize; k_g=k;
    g=(E**)calloc((size_t)n_g,sizeof(E*)); gs=(int*)calloc((size_t)n_g,sizeof(int)); int* gc=(int*)calloc((size_t)n_g,sizeof(int));
    int l=INT_MAX, r=0;
    for(int i=0;i<edgesSize;i++){
        int u=edges[i][0],v=edges[i][1],w=edges[i][2];
        if(!online[u]||!online[v]) continue;
        if(gs[u]==gc[u]){gc[u]=gc[u]?gc[u]*2:4; g[u]=realloc(g[u],(size_t)gc[u]*sizeof(E));}
        g[u][gs[u]++]=(E){v,w}; if(w<l)l=w; if(w>r)r=w;
    }
    if(l==INT_MAX){ for(int i=0;i<n_g;i++)free(g[i]); free(g);free(gs);free(gc); return -1; }
    while(l<r){ int mid=(l+r+1)>>1; if(check(mid)) l=mid; else r=mid-1; }
    int ans=check(l)?l:-1;
    for(int i=0;i<n_g;i++) free(g[i]); free(g);free(gs);free(gc);
    return ans;
}
