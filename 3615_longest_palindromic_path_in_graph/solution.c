// LeetCode 3615 - Longest Palindromic Path in Graph
// https://leetcode.com/problems/longest-palindromic-path-in-graph/

#include <stdlib.h>
#include <stdbool.h>
#include <string.h>
static int imin(int a,int b){return a<b?a:b;}
static int imax(int a,int b){return a>b?a:b;}
static int** g; static int* gs; static char* label_g; static int n_g;
static int expandPal(int l, int r){
    typedef struct { int a,b; } P;
    typedef struct { int l,r,len; } S;
    bool* vis=(bool*)calloc((size_t)n_g*n_g,sizeof(bool));
    S* q=(S*)malloc((size_t)n_g*n_g*sizeof(S)); int qh=0,qt=0;
    int len0 = l==r?1:2; q[qt++]=(S){l,r,len0};
    vis[imin(l,r)*n_g+imax(l,r)]=true; int best=len0;
    while(qh<qt){
        S cur=q[qh++];
        for(int i=0;i<gs[cur.l];i++) for(int j=0;j<gs[cur.r];j++){
            int a=g[cur.l][i], b=g[cur.r][j];
            if(a==b || label_g[a]!=label_g[b]) continue;
            int key=imin(a,b)*n_g+imax(a,b);
            if(vis[key]) continue; vis[key]=true;
            int nl=cur.len+2; if(nl>best) best=nl;
            q[qt++]=(S){a,b,nl};
        }
    }
    free(vis); free(q); return best;
}
int maxLen(int n, int** edges, int edgesSize, int* edgesColSize, char* label) {
    (void)edgesColSize; n_g=n; label_g=label;
    g=(int**)calloc((size_t)n,sizeof(int*)); gs=(int*)calloc((size_t)n,sizeof(int)); int* gc=(int*)calloc((size_t)n,sizeof(int));
    for(int i=0;i<edgesSize;i++){
        int u=edges[i][0],v=edges[i][1];
        for(int r=0;r<2;r++){ int a=r?v:u,b=r?u:v; if(gs[a]==gc[a]){gc[a]=gc[a]?gc[a]*2:4;g[a]=realloc(g[a],(size_t)gc[a]*sizeof(int));} g[a][gs[a]++]=b; }
    }
    int ans=1;
    for(int i=0;i<n;i++){ ans=imax(ans,expandPal(i,i));
        for(int j=0;j<gs[i];j++){ int v=g[i][j]; if(i<v && label[i]==label[v]) ans=imax(ans,expandPal(i,v)); }
    }
    for(int i=0;i<n;i++) free(g[i]); free(g);free(gs);free(gc);
    return ans;
}
