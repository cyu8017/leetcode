// LeetCode 3661 - Maximum Walls Destroyed by Robots
// https://leetcode.com/problems/maximum-walls-destroyed-by-robots/

#include <stdlib.h>
typedef struct { int x,d; } Pair;
static int cmp_p(const void*a,const void*b){return ((const Pair*)a)->x-((const Pair*)b)->x;}
static int cmp_int(const void*a,const void*b){return *(const int*)a-*(const int*)b;}
static int imax(int a,int b){return a>b?a:b;}
static int imin(int a,int b){return a<b?a:b;}
static int lower_bound(int* a,int n,int x){ int lo=0,hi=n; while(lo<hi){int mid=(lo+hi)/2; if(a[mid]<x) lo=mid+1; else hi=mid;} return lo; }
static Pair* arr; static int* walls; static int wn, nn;
static int memo[1005][2]; static char seen[1005][2];
static int dfs(int i, int j){
    if(i<0) return 0;
    if(seen[i][j]) return memo[i][j];
    int left=arr[i].x-arr[i].d; if(i>0) left=imax(left, arr[i-1].x+1);
    int l=lower_bound(walls,wn,left), r=lower_bound(walls,wn,arr[i].x+1);
    int ans=dfs(i-1,0)+(r-l);
    int right=arr[i].x+arr[i].d;
    if(i+1<nn){ if(j==0) right=imin(right, arr[i+1].x-arr[i+1].d-1); else right=imin(right, arr[i+1].x-1); }
    l=lower_bound(walls,wn,arr[i].x); r=lower_bound(walls,wn,right+1);
    ans=imax(ans, dfs(i-1,1)+(r-l));
    seen[i][j]=1; return memo[i][j]=ans;
}
int maxWalls(int* robots, int robotsSize, int* distance, int distanceSize, int* wallsArr, int wallsSize) {
    (void)distanceSize; nn=robotsSize; wn=wallsSize; walls=wallsArr;
    arr=(Pair*)malloc((size_t)nn*sizeof(Pair));
    for(int i=0;i<nn;i++) arr[i]=(Pair){robots[i],distance[i]};
    qsort(arr,(size_t)nn,sizeof(Pair),cmp_p);
    qsort(walls,(size_t)wn,sizeof(int),cmp_int);
    for(int i=0;i<nn;i++){ seen[i][0]=seen[i][1]=0; }
    int ans=dfs(nn-1,1); free(arr); return ans;
}
