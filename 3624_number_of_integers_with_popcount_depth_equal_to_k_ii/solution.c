// LeetCode 3624 - Number of Integers With Popcount Depth Equal to K II
// https://leetcode.com/problems/number-of-integers-with-popcount-depth-equal-to-k-ii/

#include <stdlib.h>
static int popcnt64(unsigned long long x){ int c=0; while(x){c+=x&1;x>>=1;} return c; }
static int depth(long long x){ if(x==1) return 0; int d=0; while(x>1){ x=popcnt64((unsigned long long)x); d++; } return d; }
int* popcountDepth(long long* nums, int numsSize, long long** queries, int queriesSize, int* queriesColSize, int* returnSize) {
    (void)queriesColSize;
    long long* a=(long long*)malloc((size_t)numsSize*sizeof(long long));
    for(int i=0;i<numsSize;i++) a[i]=nums[i];
    int* ans=(int*)malloc((size_t)queriesSize*sizeof(int)); int an=0;
    for(int qi=0;qi<queriesSize;qi++){
        if(queries[qi][0]==1){
            int l=(int)queries[qi][1], r=(int)queries[qi][2], k=(int)queries[qi][3], cnt=0;
            for(int i=l;i<=r;i++) if(depth(a[i])==k) cnt++;
            ans[an++]=cnt;
        } else a[(int)queries[qi][1]]=queries[qi][2];
    }
    free(a); *returnSize=an; return ans;
}
