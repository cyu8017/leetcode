// LeetCode 3649 - Number of Perfect Pairs
// https://leetcode.com/problems/number-of-perfect-pairs/

#include <stdlib.h>
static int cmp_int(const void*a,const void*b){return *(const int*)a-*(const int*)b;}
long long perfectPairs(int* nums, int numsSize) {
    int n=numsSize; int* a=(int*)malloc((size_t)n*sizeof(int));
    for(int i=0;i<n;i++) a[i]=nums[i]<0?-nums[i]:nums[i];
    qsort(a,(size_t)n,sizeof(int),cmp_int);
    long long ans=0; int j=0;
    for(int i=0;i<n;i++){ if(j<i+1) j=i+1; while(j<n && a[j]<=2*a[i]) j++; ans+=j-i-1; }
    free(a); return ans;
}
