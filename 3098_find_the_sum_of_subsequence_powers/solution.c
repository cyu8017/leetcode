// LeetCode 3098 - Find the Sum of Subsequence Powers
// https://leetcode.com/problems/find-the-sum-of-subsequence-powers/

#include <stdlib.h>
#include <stdbool.h>
#include <limits.h>

typedef struct { long long key; int val; bool used; } HEnt;
static unsigned hash_ll(unsigned long long x) {
    x ^= x >> 30; x *= 0xbf58476d1ce4e5b9ULL; x ^= x >> 27; x *= 0x94d049bb133111ebULL; x ^= x >> 31;
    return (unsigned)x;
}
static bool hget(HEnt* t, int cap, long long key, int* out) {
    unsigned h = hash_ll((unsigned long long)key) & (unsigned)(cap - 1);
    while (t[h].used) {
        if (t[h].key == key) { *out = t[h].val; return true; }
        h = (h + 1) & (unsigned)(cap - 1);
    }
    return false;
}
static void hset(HEnt* t, int cap, long long key, int val) {
    unsigned h = hash_ll((unsigned long long)key) & (unsigned)(cap - 1);
    while (t[h].used) {
        if (t[h].key == key) { t[h].val = val; return; }
        h = (h + 1) & (unsigned)(cap - 1);
    }
    t[h].used = true; t[h].key = key; t[h].val = val;
}
static int cmp_int(const void* a, const void* b) { return (*(const int*)a) - (*(const int*)b); }
static int imin(int a, int b) { return a < b ? a : b; }

static int* nums3098;
static int n3098;
static HEnt* memo3098;
static int cap3098;
static const int MOD3098 = 1000000007;

static int dfs3098(int i, int j, int k, int mi) {
    if (i >= n3098) return k == 0 ? mi : 0;
    if (n3098 - i < k) return 0;
    long long key = ((long long)mi << 18) | ((long long)i << 12) | ((long long)j << 6) | k;
    int cached;
    if (hget(memo3098, cap3098, key, &cached)) return cached;
    int ans = dfs3098(i + 1, j, k, mi);
    if (j == n3098) ans = (ans + dfs3098(i + 1, i, k - 1, mi)) % MOD3098;
    else ans = (ans + dfs3098(i + 1, i, k - 1, imin(mi, nums3098[i] - nums3098[j]))) % MOD3098;
    hset(memo3098, cap3098, key, ans);
    return ans;
}

int sumOfPowers(int* nums, int numsSize, int k) {
    qsort(nums, (size_t)numsSize, sizeof(int), cmp_int);
    nums3098 = nums; n3098 = numsSize;
    cap3098 = 1 << 20;
    memo3098 = (HEnt*)calloc((size_t)cap3098, sizeof(HEnt));
    int ans = dfs3098(0, n3098, k, INT_MAX);
    free(memo3098);
    return ans;
}
