// LeetCode 3608 - Minimum Time for K Connected Components
// https://leetcode.com/problems/minimum-time-for-k-connected-components/

#include <stdlib.h>
typedef struct { int* p; int* size; } UF;
static UF* uf_new(int n){ UF* u=malloc(sizeof(UF)); u->p=malloc((size_t)n*sizeof(int)); u->size=malloc((size_t)n*sizeof(int)); for(int i=0;i<n;i++){u->p[i]=i;u->size[i]=1;} return u; }
static int find(UF* u,int x){ return u->p[x]==x?x:(u->p[x]=find(u,u->p[x])); }
static int unite(UF* u,int a,int b){ int pa=find(u,a),pb=find(u,b); if(pa==pb) return 0; if(u->size[pa]>u->size[pb]){u->p[pb]=pa;u->size[pa]+=u->size[pb];} else {u->p[pa]=pb;u->size[pb]+=u->size[pa];} return 1; }
static int cmp_e(const void* a,const void* b){ int* const* pa=(int* const*)a; int* const* pb=(int* const*)b; return (*pa)[2]-(*pb)[2]; }
int minTime(int n, int** edges, int edgesSize, int* edgesColSize, int k) {
    (void)edgesColSize;
    qsort(edges,(size_t)edgesSize,sizeof(int*),cmp_e);
    UF* uf=uf_new(n); int cnt=n;
    for(int i=edgesSize-1;i>=0;i--){
        if(unite(uf,edges[i][0],edges[i][1])){ cnt--; if(cnt<k){ int t=edges[i][2]; free(uf->p);free(uf->size);free(uf); return t; } }
    }
    free(uf->p);free(uf->size);free(uf); return 0;
}
