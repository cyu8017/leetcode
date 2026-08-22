// LeetCode 2958 - Length of Longest Subarray With at Most K Frequency
// https://leetcode.com/problems/length-of-longest-subarray-with-at-most-k-frequency/

#include <stdlib.h>

typedef struct { int key, cnt; } KV;

int maxSubarrayLength(int* nums, int numsSize, int k) {
    KV* freq = (KV*)malloc(numsSize * sizeof(KV));
    int fn = 0, ans = 0, left = 0;
    for (int right = 0; right < numsSize; right++) {
        int v = nums[right], found = -1;
        for (int j = 0; j < fn; j++) if (freq[j].key == v) { found = j; break; }
        if (found >= 0) freq[found].cnt++;
        else { freq[fn].key = v; freq[fn].cnt = 1; found = fn++; }
        while (freq[found].cnt > k) {
            int lv = nums[left++];
            for (int j = 0; j < fn; j++) if (freq[j].key == lv) { freq[j].cnt--; break; }
            /* refresh found for v */
            for (int j = 0; j < fn; j++) if (freq[j].key == v) { found = j; break; }
        }
        if (right - left + 1 > ans) ans = right - left + 1;
    }
    free(freq);
    return ans;
}
