// LeetCode 3845 - Maximum Subarray XOR with Bounded Range
// https://leetcode.com/problems/maximum-subarray-xor-with-bounded-range/

#include <stdlib.h>

typedef struct { int next[2]; int count; } XorNode3845;

static int add_node(XorNode3845** nodes, int* nsz, int* ncap) {
    if (*nsz == *ncap) {
        *ncap = *ncap ? *ncap * 2 : 32;
        *nodes = (XorNode3845*)realloc(*nodes, (size_t)(*ncap) * sizeof(XorNode3845));
    }
    (*nodes)[*nsz].next[0] = (*nodes)[*nsz].next[1] = 0;
    (*nodes)[*nsz].count = 0;
    return (*nsz)++;
}

int maxSubarrayXor(int* nums, int numsSize, int k) {
    XorNode3845* nodes = NULL;
    int nsz = 0, ncap = 0;
    add_node(&nodes, &nsz, &ncap);
    #define ADD(x, delta) do { \
        int u = 0; nodes[u].count += (delta); \
        for (int b = 15; b >= 0; b--) { \
            int bit = ((x) >> b) & 1; \
            if (nodes[u].next[bit] == 0) nodes[u].next[bit] = add_node(&nodes, &nsz, &ncap); \
            u = nodes[u].next[bit]; nodes[u].count += (delta); \
        } \
    } while (0)
    #define QUERY(x) ({ \
        int u = 0, res = 0; \
        for (int b = 15; b >= 0; b--) { \
            int bit = ((x) >> b) & 1; \
            int want = bit ^ 1; \
            int v = nodes[u].next[want]; \
            if (v != 0 && nodes[v].count > 0) { res |= 1 << b; u = v; } \
            else u = nodes[u].next[bit]; \
        } \
        res; \
    })
    /* portable query without statement expr */
#undef QUERY
    int n = numsSize;
    int* pref = (int*)malloc((size_t)(n + 1) * sizeof(int));
    pref[0] = 0;
    for (int i = 0; i < n; i++) pref[i + 1] = pref[i] ^ nums[i];
    int* maxQ = (int*)malloc((size_t)n * sizeof(int));
    int* minQ = (int*)malloc((size_t)n * sizeof(int));
    int mh = 0, mt = 0, nh = 0, nt = 0;
    int left = 0, trieLeft = 0, ans = 0;
    for (int r = 0; r < n; r++) {
        int x = nums[r];
        while (mt > mh && nums[maxQ[mt - 1]] <= x) mt--;
        maxQ[mt++] = r;
        while (nt > nh && nums[minQ[nt - 1]] >= x) nt--;
        minQ[nt++] = r;
        while (nums[maxQ[mh]] - nums[minQ[nh]] > k) {
            if (maxQ[mh] == left) mh++;
            if (minQ[nh] == left) nh++;
            left++;
        }
        ADD(pref[r], 1);
        while (trieLeft < left) { ADD(pref[trieLeft], -1); trieLeft++; }
        {
            int xx = pref[r + 1];
            int u = 0, res = 0;
            for (int b = 15; b >= 0; b--) {
                int bit = (xx >> b) & 1;
                int want = bit ^ 1;
                int v = nodes[u].next[want];
                if (v != 0 && nodes[v].count > 0) { res |= 1 << b; u = v; }
                else u = nodes[u].next[bit];
            }
            if (res > ans) ans = res;
        }
    }
#undef ADD
    free(nodes); free(pref); free(maxQ); free(minQ);
    return ans;
}
