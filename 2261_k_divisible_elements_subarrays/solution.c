// LeetCode 2261 - K Divisible Elements Subarrays
// https://leetcode.com/problems/k-divisible-elements-subarrays/

#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

// Use rolling hash set for distinct subarrays
#define HASH_SIZE 200003

typedef struct {
    unsigned long long h;
    int len;
    int start;
    bool used;
} Entry;

static bool same_sub(int* nums, int a, int b, int len) {
    for (int i = 0; i < len; i++) {
        if (nums[a + i] != nums[b + i]) return false;
    }
    return true;
}

int countDistinct(int* nums, int numsSize, int k, int p) {
    Entry* table = (Entry*)calloc(HASH_SIZE, sizeof(Entry));
    int ans = 0;
    for (int i = 0; i < numsSize; i++) {
        int div = 0;
        unsigned long long h = 0;
        for (int j = i; j < numsSize; j++) {
            if (nums[j] % p == 0) div++;
            if (div > k) break;
            h = h * 1000003ull + (unsigned long long)(nums[j] + 1);
            int len = j - i + 1;
            unsigned slot = (unsigned)(h % HASH_SIZE);
            bool found = false;
            for (int t = 0; t < HASH_SIZE; t++) {
                unsigned idx = (slot + (unsigned)t) % HASH_SIZE;
                if (!table[idx].used) {
                    table[idx].used = true;
                    table[idx].h = h;
                    table[idx].len = len;
                    table[idx].start = i;
                    ans++;
                    found = true;
                    break;
                }
                if (table[idx].h == h && table[idx].len == len &&
                    same_sub(nums, table[idx].start, i, len)) {
                    found = true;
                    break;
                }
            }
            (void)found;
        }
    }
    free(table);
    return ans;
}
