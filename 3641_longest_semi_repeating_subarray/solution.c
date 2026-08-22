// LeetCode 3641 - Longest Semi-Repeating Subarray
// https://leetcode.com/problems/longest-semi-repeating-subarray/

#include <stdlib.h>
static int imax(int a,int b){return a>b?a:b;}
int longestSubarray(int* nums, int numsSize, int k) {
    /* hash map open address */
    typedef struct { int key, val, used; } E;
    int cap = 8192;
    E* cnt = (E*)calloc((size_t)cap, sizeof(E));
    #define GET(k,out) do{unsigned h=((unsigned)(k)*2654435761u)%(unsigned)cap;while(cnt[h].used&&cnt[h].key!=(k))h=(h+1)%(unsigned)cap;if(!cnt[h].used){cnt[h].used=1;cnt[h].key=(k);cnt[h].val=0;} out=&cnt[h].val;}while(0)
    int ans = 0, cur = 0, l = 0;
    for (int r = 0; r < numsSize; r++) {
        int* p; GET(nums[r], p); (*p)++; if (*p == 2) cur++;
        while (cur > k) {
            int* q; GET(nums[l], q); (*q)--; if (*q == 1) cur--;
            l++;
        }
        ans = imax(ans, r - l + 1);
    }
    free(cnt);
    return ans;
}
