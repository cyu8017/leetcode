// LeetCode 3656 - Determine if a Simple Graph Exists
// https://leetcode.com/problems/determine-if-a-simple-graph-exists/

#include <stdlib.h>
#include <stdbool.h>
static int cmp_rev(const void*a,const void*b){return *(const int*)b-*(const int*)a;}
bool simpleGraphExists(int* degrees, int degreesSize) {
    int n=degreesSize; int* d=(int*)malloc((size_t)n*sizeof(int)); for(int i=0;i<n;i++) d[i]=degrees[i];
    qsort(d,(size_t)n,sizeof(int),cmp_rev);
    long long sum=0; for(int i=0;i<n;i++){ if(d[i]<0||d[i]>=n){free(d);return false;} sum+=d[i]; }
    if(sum%2){ free(d); return false; }
    long long* prefix=(long long*)calloc((size_t)n+1,sizeof(long long));
    for(int i=0;i<n;i++) prefix[i+1]=prefix[i]+d[i];
    for(int k=1;k<=n;k++){
        long long right=0; for(int i=k;i<n;i++) right += d[i]<k ? d[i] : k;
        if(prefix[k] > (long long)k*(k-1)+right){ free(d); free(prefix); return false; }
    }
    free(d); free(prefix); return true;
}
