// LeetCode 3587 - Minimum Adjacent Swaps to Alternate Parity
// https://leetcode.com/problems/minimum-adjacent-swaps-to-alternate-parity/

#include <stdlib.h>
static int iabs(int x){return x<0?-x:x;}
static int imin(int a,int b){return a<b?a:b;}
int minSwaps(int* nums, int numsSize) {
    int* pos0=(int*)malloc((size_t)numsSize*sizeof(int));
    int* pos1=(int*)malloc((size_t)numsSize*sizeof(int));
    int n0=0,n1=0;
    for(int i=0;i<numsSize;i++){ if(nums[i]&1) pos1[n1++]=i; else pos0[n0++]=i; }
    if(iabs(n0-n1)>1){ free(pos0);free(pos1); return -1; }
    int calc(int* pos, int pn){ int res=0; for(int i=0;i<numsSize;i+=2) res+=iabs(pos[i/2]-i); return res; }
    int ans;
    if(n0>n1) ans=calc(pos0,n0);
    else if(n0<n1) ans=calc(pos1,n1);
    else ans=imin(calc(pos0,n0), calc(pos1,n1));
    free(pos0); free(pos1); return ans;
}
