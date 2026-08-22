// LeetCode 3850 - Count Sequences To K
// https://leetcode.com/problems/count-sequences-to-k/

#include <stdlib.h>

typedef struct { int i; long long p, q; int val; int used; } Memo3850;

static long long gcdll(long long a, long long b) {
    while (b) { long long t = a % b; a = b; b = t; }
    return a;
}

static int* nums3850;
static int n3850;
static long long k3850;
static Memo3850* memo3850;
static int mcap3850;

static unsigned hash3850(int i, long long p, long long q) {
    unsigned h = (unsigned)i;
    h = h * 1000003u + (unsigned)(p ^ (p >> 32));
    h = h * 1000003u + (unsigned)(q ^ (q >> 32));
    return h;
}

static int dfs3850(int i, long long p, long long q) {
    if (i == n3850) return (p == k3850 && q == 1) ? 1 : 0;
    unsigned h = hash3850(i, p, q) % (unsigned)mcap3850;
    for (int t = 0; t < mcap3850; t++) {
        int j = (int)((h + t) % (unsigned)mcap3850);
        if (!memo3850[j].used) break;
        if (memo3850[j].i == i && memo3850[j].p == p && memo3850[j].q == q) return memo3850[j].val;
    }
    int res = dfs3850(i + 1, p, q);
    long long x = nums3850[i];
    long long g1 = gcdll(p * x, q);
    res += dfs3850(i + 1, (p * x) / g1, q / g1);
    long long g2 = gcdll(p, q * x);
    res += dfs3850(i + 1, p / g2, (q * x) / g2);
    h = hash3850(i, p, q) % (unsigned)mcap3850;
    for (int t = 0; t < mcap3850; t++) {
        int j = (int)((h + t) % (unsigned)mcap3850);
        if (!memo3850[j].used) {
            memo3850[j].used = 1; memo3850[j].i = i; memo3850[j].p = p; memo3850[j].q = q; memo3850[j].val = res;
            break;
        }
        if (memo3850[j].i == i && memo3850[j].p == p && memo3850[j].q == q) { memo3850[j].val = res; break; }
    }
    return res;
}

int countSequences(int* nums, int numsSize, long long k) {
    nums3850 = nums; n3850 = numsSize; k3850 = k;
    mcap3850 = 1;
    while (mcap3850 < numsSize * 64 + 64) mcap3850 <<= 1;
    memo3850 = (Memo3850*)calloc((size_t)mcap3850, sizeof(Memo3850));
    int ans = dfs3850(0, 1, 1);
    free(memo3850);
    return ans;
}
