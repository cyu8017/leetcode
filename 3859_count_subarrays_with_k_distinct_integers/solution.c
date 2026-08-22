// LeetCode 3859 - Count Subarrays With K Distinct Integers
// https://leetcode.com/problems/count-subarrays-with-k-distinct-integers/

#include <stdlib.h>
#include <string.h>

long long countSubarrays(int* nums, int numsSize, int k, int m) {
    long long result[2];
    for (int pass = 0; pass < 2; pass++) {
        int lim = k + pass;
        int cap = 1;
        while (cap < numsSize * 2 + 16) cap <<= 1;
        int* keys = (int*)malloc((size_t)cap * sizeof(int));
        int* vals = (int*)calloc((size_t)cap, sizeof(int));
        char* used = (char*)calloc((size_t)cap, 1);
        int distinct = 0;
        long long ans = 0;
        int lpos = 0, t = 0;
        for (int r = 0; r < numsSize; r++) {
            int x = nums[r];
            unsigned h = (unsigned)x * 2654435761u;
            int j = (int)(h & (unsigned)(cap - 1));
            while (used[j] && keys[j] != x) j = (j + 1) & (cap - 1);
            if (!used[j]) { used[j] = 1; keys[j] = x; vals[j] = 0; distinct++; }
            vals[j]++;
            if (vals[j] == m) t++;
            while (distinct >= lim && t >= k) {
                int y = nums[lpos++];
                h = (unsigned)y * 2654435761u;
                j = (int)(h & (unsigned)(cap - 1));
                while (used[j] && keys[j] != y) j = (j + 1) & (cap - 1);
                vals[j]--;
                if (vals[j] == m - 1) t--;
                if (vals[j] == 0) { used[j] = 0; distinct--; }
            }
            ans += lpos;
        }
        result[pass] = ans;
        free(keys); free(vals); free(used);
    }
    return result[0] - result[1];
}
