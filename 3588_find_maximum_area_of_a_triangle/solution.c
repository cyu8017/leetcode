// LeetCode 3588 - Find Maximum Area of a Triangle
// https://leetcode.com/problems/find-maximum-area-of-a-triangle/

#include <stdlib.h>
static int imin(int a,int b){return a<b?a:b;}
static int imax(int a,int b){return a>b?a:b;}
static long long llmax(long long a,long long b){return a>b?a:b;}
static long long calc(int** coords, int n) {
    int mn=1000000000, mx=0;
    /* store min/max y per x via arrays of pairs */
    int* xs=(int*)malloc((size_t)n*sizeof(int));
    int* ymin=(int*)malloc((size_t)n*sizeof(int));
    int* ymax=(int*)malloc((size_t)n*sizeof(int));
    int m=0;
    for(int i=0;i<n;i++){
        int x=coords[i][0], y=coords[i][1];
        mn=imin(mn,x); mx=imax(mx,x);
        int found=-1; for(int j=0;j<m;j++) if(xs[j]==x){found=j;break;}
        if(found<0){ xs[m]=x; ymin[m]=ymax[m]=y; m++; }
        else { ymin[found]=imin(ymin[found],y); ymax[found]=imax(ymax[found],y); }
    }
    long long ans=0;
    for(int i=0;i<m;i++){
        int d=ymax[i]-ymin[i];
        ans=llmax(ans, (long long)d * imax(mx-xs[i], xs[i]-mn));
    }
    free(xs);free(ymin);free(ymax);
    return ans;
}
long long maxArea(int** coords, int coordsSize, int* coordsColSize) {
    (void)coordsColSize;
    long long ans=calc(coords, coordsSize);
    for(int i=0;i<coordsSize;i++){ int t=coords[i][0]; coords[i][0]=coords[i][1]; coords[i][1]=t; }
    ans=llmax(ans, calc(coords, coordsSize));
    for(int i=0;i<coordsSize;i++){ int t=coords[i][0]; coords[i][0]=coords[i][1]; coords[i][1]=t; }
    return ans>0?ans:-1;
}
