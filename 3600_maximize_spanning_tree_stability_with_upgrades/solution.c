// LeetCode 3600 - Maximize Spanning Tree Stability with Upgrades
// https://leetcode.com/problems/maximize-spanning-tree-stability-with-upgrades/

#include <stdlib.h>
typedef struct { int* p; int* size; int cnt; } UF;
static UF* uf_new(int n){ UF* u=malloc(sizeof(UF)); u->p=malloc((size_t)n*sizeof(int)); u->size=malloc((size_t)n*sizeof(int)); u->cnt=n; for(int i=0;i<n;i++){u->p[i]=i;u->size[i]=1;} return u; }
static int uf_find(UF* u,int x){ return u->p[x]==x?x:(u->p[x]=uf_find(u,u->p[x])); }
static int uf_union(UF* u,int a,int b){ int pa=uf_find(u,a),pb=uf_find(u,b); if(pa==pb) return 0; if(u->size[pa]>u->size[pb]){u->p[pb]=pa;u->size[pa]+=u->size[pb];} else {u->p[pa]=pb;u->size[pb]+=u->size[pa];} u->cnt--; return 1; }
static void uf_free(UF* u){ free(u->p); free(u->size); free(u); }
static int N_g,K_g; static int** E_g; static int ES;
static int check(int lim){
    UF* uf=uf_new(N_g);
    for(int i=0;i<ES;i++) if(E_g[i][2]>=lim) uf_union(uf,E_g[i][0],E_g[i][1]);
    int rem=K_g;
    for(int i=0;i<ES;i++) if(E_g[i][2]*2>=lim && rem>0) if(uf_union(uf,E_g[i][0],E_g[i][1])) rem--;
    int ok=uf->cnt==1; uf_free(uf); return ok;
}
int maxStability(int n, int** edges, int edgesSize, int* edgesColSize, int k) {
    (void)edgesColSize;
    N_g=n; E_g=edges; ES=edgesSize; K_g=k;
    UF* uf=uf_new(n); int mn=1000000;
    for(int i=0;i<edgesSize;i++){
        int u=edges[i][0],v=edges[i][1],s=edges[i][2],must=edges[i][3];
        if(must==1){ if(s<mn) mn=s; if(!uf_union(uf,u,v)){ uf_free(uf); return -1; } }
    }
    for(int i=0;i<edgesSize;i++) uf_union(uf,edges[i][0],edges[i][1]);
    if(uf->cnt>1){ uf_free(uf); return -1; }
    uf_free(uf);
    int l=1,r=mn;
    while(l<r){ int mid=(l+r+1)>>1; if(check(mid)) l=mid; else r=mid-1; }
    return l;
}
