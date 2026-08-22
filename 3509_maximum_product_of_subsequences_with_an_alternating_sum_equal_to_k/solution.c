// LeetCode 3509 - Maximum Product of Subsequences With an Alternating Sum Equal to K
// https://leetcode.com/problems/maximum-product-of-subsequences-with-an-alternating-sum-equal-to-k/

#include <stdlib.h>

#define MIN3509 (-5000)

static int *nums3509, n3509, limit3509;
/* memo with open addressing: key packed */
typedef struct { int key; int val; char used; } M3509;
static M3509* memo3509;
static int mcap3509;

static int abs3509(int x) { return x < 0 ? -x : x; }
static int max3509(int a, int b) { return a > b ? a : b; }

static int pack(int i, int product, int state, int kk) {
    /* product can be up to limit+1, kk offset by 5000 */
    return (((i * 64 + product) * 4 + state) * 10001 + (kk + 5000));
}

static int memoGet(int key, int* found) {
    unsigned h = (unsigned)key % (unsigned)mcap3509;
    for (int t = 0; t < mcap3509; t++) {
        int j = (h + t) % mcap3509;
        if (!memo3509[j].used) { *found = 0; return 0; }
        if (memo3509[j].key == key) { *found = 1; return memo3509[j].val; }
    }
    *found = 0; return 0;
}
static void memoPut(int key, int val) {
    unsigned h = (unsigned)key % (unsigned)mcap3509;
    for (int t = 0; t < mcap3509; t++) {
        int j = (h + t) % mcap3509;
        if (!memo3509[j].used || memo3509[j].key == key) {
            memo3509[j].used = 1; memo3509[j].key = key; memo3509[j].val = val; return;
        }
    }
}

static int dp3509(int i, int product, int state, int kk) {
    if (i == n3509) {
        if (kk == 0 && state != 0 && product <= limit3509) return product;
        return MIN3509;
    }
    int key = pack(i, product, state, kk);
    int found; int mv = memoGet(key, &found);
    if (found) return mv;
    int res = dp3509(i + 1, product, state, kk);
    if (state == 0) res = max3509(res, dp3509(i + 1, nums3509[i], 1, kk - nums3509[i]));
    if (state == 1) {
        int np = product * nums3509[i];
        if (np > limit3509 + 1) np = limit3509 + 1;
        res = max3509(res, dp3509(i + 1, np, 2, kk + nums3509[i]));
    }
    if (state == 2) {
        int np = product * nums3509[i];
        if (np > limit3509 + 1) np = limit3509 + 1;
        res = max3509(res, dp3509(i + 1, np, 1, kk - nums3509[i]));
    }
    memoPut(key, res);
    return res;
}

int maxProduct(int* nums, int numsSize, int k, int limit) {
    int sumAll = 0;
    for (int i = 0; i < numsSize; i++) sumAll += nums[i];
    if (abs3509(k) > sumAll) return -1;
    nums3509 = nums; n3509 = numsSize; limit3509 = limit;
    mcap3509 = 200003;
    memo3509 = (M3509*)calloc((size_t)mcap3509, sizeof(M3509));
    int ans = dp3509(0, 1, 0, k);
    free(memo3509);
    return ans == MIN3509 ? -1 : ans;
}
