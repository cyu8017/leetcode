// LeetCode 3613 - Minimize Maximum Component Cost
// https://leetcode.com/problems/minimize-maximum-component-cost/

#include <stdlib.h>
static int* p;
static int find(int x){ return p[x]==x?x:(p[x]=find(p[x])); }
static int cmp_e(const void* a, const void* b){
    int* const* pa=(int* const*)a; int* const* pb=(int* const*)b;
    return (*pa)[2]-(*pb)[2];
}
int minCost(int n, int** edges, int edgesSize, int* edgesColSize, int k) {
    (void)edgesColSize;
    p=(int*)malloc((size_t)n*sizeof(int)); for(int i=0;i<n;i++) p[i]=i;
    if(k==n){ free(p); return 0; }
    qsort(edges,(size_t)edgesSize,sizeof(int*),cmp_e);
    int cnt=n;
    for(int i=0;i<edgesSize;i++){
        int u=edges[i][0],v=edges[i][1],w=edges[i][2];
        int pu=find(u),pv=find(v);
        if(pu!=pv){ p[pu]=pv; if(--cnt<=k){ free(p); return w; } }
    }
    free(p); return 0;
}
