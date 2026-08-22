// LeetCode 3607 - Power Grid Maintenance
// https://leetcode.com/problems/power-grid-maintenance/

#include <stdlib.h>
#include <stdbool.h>
static int* parent;
static int find(int x){ return parent[x]==x?x:(parent[x]=find(parent[x])); }
static void unite(int a,int b){ int ra=find(a),rb=find(b); if(ra!=rb){ if(ra<rb) parent[rb]=ra; else parent[ra]=rb; } }
int* processQueries(int c, int** connections, int connectionsSize, int* connectionsColSize, int** queries, int queriesSize, int* queriesColSize, int* returnSize) {
    (void)connectionsColSize;(void)queriesColSize;
    parent=(int*)malloc((size_t)(c+1)*sizeof(int)); for(int i=0;i<=c;i++) parent[i]=i;
    for(int i=0;i<connectionsSize;i++) unite(connections[i][0],connections[i][1]);
    bool* online=(bool*)malloc((size_t)(c+1)*sizeof(bool)); for(int i=1;i<=c;i++) online[i]=true;
    int** comp=(int**)calloc((size_t)(c+1),sizeof(int*)); int* cs=(int*)calloc((size_t)(c+1),sizeof(int)); int* cc=(int*)calloc((size_t)(c+1),sizeof(int));
    for(int i=1;i<=c;i++){ int r=find(i); if(cs[r]==cc[r]){cc[r]=cc[r]?cc[r]*2:4; comp[r]=realloc(comp[r],(size_t)cc[r]*sizeof(int));} comp[r][cs[r]++]=i; }
    for(int r=1;r<=c;r++) if(cs[r]>1){ /* sort ids */ for(int i=0;i<cs[r];i++) for(int j=i+1;j<cs[r];j++) if(comp[r][j]<comp[r][i]){int t=comp[r][i];comp[r][i]=comp[r][j];comp[r][j]=t;} }
    int* ptr=(int*)calloc((size_t)(c+1),sizeof(int));
    int* ans=(int*)malloc((size_t)queriesSize*sizeof(int)); int an=0;
    for(int qi=0;qi<queriesSize;qi++){
        int t=queries[qi][0], x=queries[qi][1];
        if(t==2){ online[x]=false; continue; }
        if(online[x]){ ans[an++]=x; continue; }
        int r=find(x); int* ids=comp[r];
        while(ptr[r]<cs[r] && !online[ids[ptr[r]]]) ptr[r]++;
        ans[an++]= ptr[r]<cs[r] ? ids[ptr[r]] : -1;
    }
    for(int i=0;i<=c;i++) free(comp[i]);
    free(comp);free(cs);free(cc);free(ptr);free(online);free(parent);
    *returnSize=an; return ans;
}
