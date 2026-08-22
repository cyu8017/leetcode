// LeetCode 3590 - Kth Smallest Path XOR Sum
// https://leetcode.com/problems/kth-smallest-path-xor-sum/

#include <stdlib.h>
static int cmp_int(const void*a,const void*b){return *(const int*)a-*(const int*)b;}
static int** g; static int* gs; static int* xorPath; static int* inT; static int* outT; static int* order; static int orderN; static int* vals_g;
static void dfs(int u){ xorPath[u]^=vals_g[u]; for(int i=0;i<gs[u];i++){ int v=g[u][i]; xorPath[v]=xorPath[u]; dfs(v);} }
static void dfs2(int u){ inT[u]=orderN; order[orderN++]=xorPath[u]; for(int i=0;i<gs[u];i++) dfs2(g[u][i]); outT[u]=orderN; }
int* kthSmallest(int* par, int parSize, int* vals, int valsSize, int** queries, int queriesSize, int* queriesColSize, int* returnSize) {
    (void)parSize;(void)queriesColSize;
    int n=valsSize; vals_g=vals;
    g=(int**)calloc((size_t)n,sizeof(int*)); gs=(int*)calloc((size_t)n,sizeof(int)); int* gc=(int*)calloc((size_t)n,sizeof(int));
    for(int i=1;i<n;i++){ int p=par[i]; if(gs[p]==gc[p]){gc[p]=gc[p]?gc[p]*2:4; g[p]=realloc(g[p],(size_t)gc[p]*sizeof(int));} g[p][gs[p]++]=i; }
    xorPath=(int*)calloc((size_t)n,sizeof(int)); dfs(0);
    inT=(int*)malloc((size_t)n*sizeof(int)); outT=(int*)malloc((size_t)n*sizeof(int));
    order=(int*)malloc((size_t)n*sizeof(int)); orderN=0; dfs2(0);
    int* ans=(int*)malloc((size_t)queriesSize*sizeof(int));
    for(int i=0;i<queriesSize;i++){
        int u=queries[i][0], k=queries[i][1];
        int len=outT[u]-inT[u];
        int* sub=(int*)malloc((size_t)len*sizeof(int));
        for(int j=0;j<len;j++) sub[j]=order[inT[u]+j];
        qsort(sub,(size_t)len,sizeof(int),cmp_int);
        int un=0; for(int j=0;j<len;j++) if(un==0||sub[j]!=sub[un-1]) sub[un++]=sub[j];
        ans[i]= k>un ? -1 : sub[k-1];
        free(sub);
    }
    for(int i=0;i<n;i++) free(g[i]); free(g);free(gs);free(gc);free(xorPath);free(inT);free(outT);free(order);
    *returnSize=queriesSize; return ans;
}
