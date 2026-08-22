// LeetCode 3777 - Minimum Deletions To Make Alternating Substring
// https://leetcode.com/problems/minimum-deletions-to-make-alternating-substring/

#include <stdlib.h>
#include <string.h>

typedef struct {
    int n;
    int* c;
} BIT3777;

static BIT3777* bit_new(int n) {
    BIT3777* bit = (BIT3777*)malloc(sizeof(BIT3777));
    bit->n = n;
    bit->c = (int*)calloc((size_t)n + 1, sizeof(int));
    return bit;
}

static void bit_update(BIT3777* bit, int x, int delta) {
    for (; x <= bit->n; x += x & -x) bit->c[x] += delta;
}

static int bit_query(BIT3777* bit, int x) {
    int s = 0;
    for (; x > 0; x -= x & -x) s += bit->c[x];
    return s;
}

int* minDeletions(char* s, int** queries, int queriesSize, int* queriesColSize, int* returnSize) {
    (void)queriesColSize;
    int n = (int)strlen(s);
    int* nums = (int*)calloc((size_t)n, sizeof(int));
    BIT3777* bit = bit_new(n);
    for (int i = 1; i < n; i++) {
        if (s[i] == s[i - 1]) {
            nums[i] = 1;
            bit_update(bit, i + 1, 1);
        }
    }
    int* ans = (int*)malloc((size_t)queriesSize * sizeof(int));
    int asz = 0;
    for (int qi = 0; qi < queriesSize; qi++) {
        int* q = queries[qi];
        if (q[0] == 1) {
            int j = q[1];
            int delta = (nums[j] ^ 1) - nums[j];
            nums[j] ^= 1;
            bit_update(bit, j + 1, delta);
            if (j + 1 < n) {
                delta = (nums[j + 1] ^ 1) - nums[j + 1];
                nums[j + 1] ^= 1;
                bit_update(bit, j + 2, delta);
            }
        } else {
            int l = q[1], r = q[2];
            ans[asz++] = bit_query(bit, r + 1) - bit_query(bit, l + 1);
        }
    }
    free(nums);
    free(bit->c);
    free(bit);
    *returnSize = asz;
    return ans;
}
