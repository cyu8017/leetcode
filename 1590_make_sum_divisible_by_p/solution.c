// LeetCode 1590 - Make Sum Divisible by P
// https://leetcode.com/problems/make-sum-divisible-by-p/

#include <stdlib.h>

int minSubarray(int* nums, int numsSize, int p) {
    long long total = 0;
    for (int i = 0; i < numsSize; i++) total += nums[i];
    int target = (int)(total % p);
    if (target == 0) return 0;

    int cap = 1;
    while (cap < numsSize * 2 + 4) cap <<= 1;
    int* keys = (int*)malloc((size_t)cap * sizeof(int));
    int* vals = (int*)malloc((size_t)cap * sizeof(int));
    char* used = (char*)calloc((size_t)cap, 1);

    unsigned h0 = 0;
    used[h0] = 1;
    keys[h0] = 0;
    vals[h0] = -1;

    int prefix = 0, answer = numsSize;
    for (int i = 0; i < numsSize; i++) {
        prefix = (prefix + nums[i]) % p;
        int need = (prefix - target + p) % p;
        unsigned h = (unsigned)need % (unsigned)cap;
        while (used[h]) {
            if (keys[h] == need) {
                if (i - vals[h] < answer) answer = i - vals[h];
                break;
            }
            h = (h + 1) % (unsigned)cap;
        }
        h = (unsigned)prefix % (unsigned)cap;
        while (used[h] && keys[h] != prefix) h = (h + 1) % (unsigned)cap;
        used[h] = 1;
        keys[h] = prefix;
        vals[h] = i;
    }
    free(keys);
    free(vals);
    free(used);
    return answer < numsSize ? answer : -1;
}
