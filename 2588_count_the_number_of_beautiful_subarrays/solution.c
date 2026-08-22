// LeetCode 2588 - Count the Number of Beautiful Subarrays
// https://leetcode.com/problems/count-the-number-of-beautiful-subarrays/

#include <stdlib.h>
#include <stdbool.h>

typedef struct { int key; int val; bool set; } HM;

long long beautifulSubarrays(int* nums, int numsSize) {
    int cap = 1;
    while (cap < numsSize * 2 + 16) cap <<= 1;
    HM* freq = (HM*)calloc((size_t)cap, sizeof(HM));
    #define HPUT(k, d) do { \
        unsigned h = (unsigned)(k) & (cap - 1); \
        while (freq[h].set && freq[h].key != (k)) h = (h + 1) & (cap - 1); \
        if (!freq[h].set) { freq[h].set = true; freq[h].key = (k); freq[h].val = 0; } \
        freq[h].val += (d); \
    } while (0)
    #define HGET(k, out) do { \
        unsigned h = (unsigned)(k) & (cap - 1); \
        (out) = 0; \
        while (freq[h].set) { if (freq[h].key == (k)) { (out) = freq[h].val; break; } h = (h + 1) & (cap - 1); } \
    } while (0)
    HPUT(0, 1);
    int xorv = 0;
    long long ans = 0;
    for (int i = 0; i < numsSize; i++) {
        xorv ^= nums[i];
        int f; HGET(xorv, f);
        ans += f;
        HPUT(xorv, 1);
    }
    free(freq);
    return ans;
}
