// LeetCode 3578 - Count Partitions With Max-Min Difference at Most K
// https://leetcode.com/problems/count-partitions-with-max-min-difference-at-most-k/

#include <stdlib.h>
/* multiset via sorted dynamic array of (key,count) */
typedef struct { int key, cnt; } Node;
typedef struct { Node* a; int n, cap; } MS;
static void ms_init(MS* m){ m->a=NULL; m->n=m->cap=0; }
static void ms_free(MS* m){ free(m->a); }
static int ms_find(MS* m, int x){ for(int i=0;i<m->n;i++) if(m->a[i].key==x) return i; return -1; }
static void ms_merge(MS* m, int x, int v){
    int i=ms_find(m,x);
    if(i<0){
        if(m->n==m->cap){ m->cap=m->cap?m->cap*2:8; m->a=realloc(m->a,(size_t)m->cap*sizeof(Node)); }
        /* insert sorted */
        int j=m->n; while(j>0 && m->a[j-1].key>x){ m->a[j]=m->a[j-1]; j--; }
        m->a[j].key=x; m->a[j].cnt=v; m->n++;
    } else {
        m->a[i].cnt+=v;
        if(m->a[i].cnt==0){ for(int j=i;j<m->n-1;j++) m->a[j]=m->a[j+1]; m->n--; }
    }
}
int countPartitions(int* nums, int numsSize, int k) {
    const int mod = 1000000007;
    MS sl; ms_init(&sl);
    int n=numsSize;
    int* f=(int*)calloc((size_t)n+1,sizeof(int));
    int* g=(int*)calloc((size_t)n+1,sizeof(int));
    f[0]=g[0]=1;
    for(int l=1,r=1;r<=n;r++){
        ms_merge(&sl, nums[r-1], 1);
        while(sl.n>0 && sl.a[sl.n-1].key - sl.a[0].key > k){ ms_merge(&sl, nums[l-1], -1); l++; }
        f[r]=g[r-1];
        if(l>=2) f[r]=(f[r]-g[l-2]+mod)%mod;
        g[r]=(g[r-1]+f[r])%mod;
    }
    int ans=f[n]; free(f); free(g); ms_free(&sl); return ans;
}
