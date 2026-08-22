// LeetCode 3729 - Count Distinct Subarrays Divisible by K in Sorted Array
// https://leetcode.com/problems/count-distinct-subarrays-divisible-by-k-in-sorted-array/

#include <stdlib.h>
#include <string.h>

#define HS 200003
static int hk[HS], hv[HS];
static char hu[HS];
static void hc(void){memset(hu,0,sizeof(hu));}
static int* hg(int k){
    int i=(int)((unsigned)k%HS);
    while(hu[i]&&hk[i]!=k){if(++i==HS)i=0;}
    if(!hu[i]){hu[i]=1;hk[i]=k;hv[i]=0;}
    return &hv[i];
}
static int hget(int k){
    int i=(int)((unsigned)k%HS);
    while(hu[i]&&hk[i]!=k){if(++i==HS)i=0;}
    return hu[i]?hv[i]:0;
}

long long numGoodSubarrays(int* nums, int numsSize, int k) {
    long long ans = 0;
    int s = 0;
    hc();
    (*hg(0)) = 1;
    for (int i = 0; i < numsSize; i++) {
        s = (s + nums[i]) % k;
        ans += hget(s);
        (*hg(s))++;
    }
    int n = numsSize;
    for (int i = 0; i < n; ) {
        int j = i + 1;
        while (j < n && nums[j] == nums[i]) j++;
        int m = j - i;
        for (int h = 1; h <= m; h++) {
            if ((long long)nums[i] * h % k == 0) ans -= (m - h);
        }
        i = j;
    }
    return ans;
}
