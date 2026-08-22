// LeetCode 3761 - Minimum Absolute Distance Between Mirror Pairs
// https://leetcode.com/problems/minimum-absolute-distance-between-mirror-pairs/

#include <string.h>

#define HS 200003
static int hk[HS], hv[HS];
static char hu[HS];
static void hc(void){memset(hu,0,sizeof(hu));}
static int hhas(int k, int* out){
    int i=(int)((unsigned)k%HS);
    while(hu[i]&&hk[i]!=k){if(++i==HS)i=0;}
    if(!hu[i])return 0; *out=hv[i]; return 1;
}
static void hput(int k, int v){
    int i=(int)((unsigned)k%HS);
    while(hu[i]&&hk[i]!=k){if(++i==HS)i=0;}
    hu[i]=1; hk[i]=k; hv[i]=v;
}
static int reverse(int x) {
    int y = 0;
    for (; x > 0; x /= 10) y = y * 10 + x % 10;
    return y;
}

int minMirrorPairDistance(int* nums, int numsSize) {
    hc();
    int n = numsSize, ans = n + 1;
    for (int i = 0; i < n; i++) {
        int j;
        if (hhas(nums[i], &j)) {
            if (i - j < ans) ans = i - j;
        }
        hput(reverse(nums[i]), i);
    }
    return ans > n ? -1 : ans;
}
