// LeetCode 3651 - Minimum Cost Path with Teleportations
// https://leetcode.com/problems/minimum-cost-path-with-teleportations/

#include <stdlib.h>
#include <limits.h>
static int imin(int a,int b){return a<b?a:b;}
static int cmp_rev(const void*a,const void*b){return *(const int*)b-*(const int*)a;}
int minCost(int** grid, int gridSize, int* gridColSize, int k) {
    int m=gridSize,n=gridColSize[0], inf=INT_MAX/4;
    int*** f=(int***)malloc((size_t)(k+1)*sizeof(int**));
    for(int t=0;t<=k;t++){ f[t]=(int**)malloc((size_t)m*sizeof(int*)); for(int i=0;i<m;i++){ f[t][i]=(int*)malloc((size_t)n*sizeof(int)); for(int j=0;j<n;j++) f[t][i][j]=inf; } }
    f[0][0][0]=0;
    for(int i=0;i<m;i++) for(int j=0;j<n;j++){ if(i>0) f[0][i][j]=imin(f[0][i][j],f[0][i-1][j]+grid[i][j]); if(j>0) f[0][i][j]=imin(f[0][i][j],f[0][i][j-1]+grid[i][j]); }
    /* group positions by value */
    typedef struct { int key; int* pos; int n,cap; } G;
    G* groups=NULL; int gn=0,gcap=0;
    for(int i=0;i<m;i++) for(int j=0;j<n;j++){
        int x=grid[i][j], gi=-1; for(int t=0;t<gn;t++) if(groups[t].key==x){gi=t;break;}
        if(gi<0){ if(gn==gcap){gcap=gcap?gcap*2:8; groups=realloc(groups,(size_t)gcap*sizeof(G));} groups[gn]=(G){x,NULL,0,0}; gi=gn++; }
        if(groups[gi].n==groups[gi].cap){ groups[gi].cap=groups[gi].cap?groups[gi].cap*2:4; groups[gi].pos=realloc(groups[gi].pos,(size_t)groups[gi].cap*2*sizeof(int)); }
        groups[gi].pos[groups[gi].n*2]=i; groups[gi].pos[groups[gi].n*2+1]=j; groups[gi].n++;
    }
    int* keys=(int*)malloc((size_t)gn*sizeof(int)); for(int i=0;i<gn;i++) keys[i]=groups[i].key;
    qsort(keys,(size_t)gn,sizeof(int),cmp_rev);
    for(int t=1;t<=k;t++){
        int mn=inf;
        for(int ki=0;ki<gn;ki++){
            int key=keys[ki], gi=-1; for(int z=0;z<gn;z++) if(groups[z].key==key){gi=z;break;}
            for(int p=0;p<groups[gi].n;p++){ int ii=groups[gi].pos[p*2], jj=groups[gi].pos[p*2+1]; mn=imin(mn,f[t-1][ii][jj]); }
            for(int p=0;p<groups[gi].n;p++){ int ii=groups[gi].pos[p*2], jj=groups[gi].pos[p*2+1]; f[t][ii][jj]=mn; }
        }
        for(int i=0;i<m;i++) for(int j=0;j<n;j++){ if(i>0) f[t][i][j]=imin(f[t][i][j],f[t][i-1][j]+grid[i][j]); if(j>0) f[t][i][j]=imin(f[t][i][j],f[t][i][j-1]+grid[i][j]); }
    }
    int ans=inf; for(int t=0;t<=k;t++) ans=imin(ans,f[t][m-1][n-1]);
    for(int t=0;t<=k;t++){ for(int i=0;i<m;i++) free(f[t][i]); free(f[t]); } free(f);
    for(int i=0;i<gn;i++) free(groups[i].pos); free(groups); free(keys);
    return ans;
}
