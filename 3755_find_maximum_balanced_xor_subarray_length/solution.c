// LeetCode 3755 - Find Maximum Balanced Xor Subarray Length
// https://leetcode.com/problems/find-maximum-balanced-xor-subarray-length/

#include <string.h>

#define HS 200003
static long long hk[HS];
static int hv[HS];
static char hu[HS];
static void hc(void){memset(hu,0,sizeof(hu));}
static int hhas(long long k, int* out){
    unsigned i=(unsigned)((k%HS+HS)%HS);
    for(;;){if(!hu[i])return 0;if(hk[i]==k){*out=hv[i];return 1;}if(++i==HS)i=0;}
}
static void hput(long long k, int v){
    unsigned i=(unsigned)((k%HS+HS)%HS);
    for(;;){if(!hu[i]){hu[i]=1;hk[i]=k;hv[i]=v;return;}if(hk[i]==k){hv[i]=v;return;}if(++i==HS)i=0;}
}

int maxBalancedSubarray(int* nums, int numsSize) {
    hc();
    int a = 0, b = numsSize, ans = 0;
    hput((long long)b, -1);
    for (int i = 0; i < numsSize; i++) {
        a ^= nums[i];
        if (nums[i] % 2 == 0) b++; else b--;
        long long key = ((long long)a << 32) | (unsigned)b;
        int j;
        if (hhas(key, &j)) {
            if (i - j > ans) ans = i - j;
        } else hput(key, i);
    }
    return ans;
}
