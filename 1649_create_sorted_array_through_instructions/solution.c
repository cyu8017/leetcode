// LeetCode 1649 - Create Sorted Array through Instructions
// https://leetcode.com/problems/create-sorted-array-through-instructions/

#include <stdlib.h>

#define MOD 1000000007

static int bitQuery(int* bit, int i) {
    int s = 0;
    while (i > 0) {
        s += bit[i];
        i -= i & -i;
    }
    return s;
}

static void bitUpdate(int* bit, int size, int i, int delta) {
    while (i <= size) {
        bit[i] += delta;
        i += i & -i;
    }
}

int createSortedArray(int* instructions, int instructionsSize) {
    int mx = 0;
    for (int i = 0; i < instructionsSize; i++) if (instructions[i] > mx) mx = instructions[i];
    int size = mx + 2;
    int* bit = (int*)calloc((size_t)(size + 1), sizeof(int));
    long long ans = 0;
    for (int i = 0; i < instructionsSize; i++) {
        int x = instructions[i];
        int less = bitQuery(bit, x - 1);
        int greater = i - bitQuery(bit, x);
        int cost = less < greater ? less : greater;
        ans = (ans + cost) % MOD;
        bitUpdate(bit, size, x, 1);
    }
    free(bit);
    return (int)ans;
}
