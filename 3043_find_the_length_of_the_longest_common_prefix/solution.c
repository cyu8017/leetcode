// LeetCode 3043 - Find the Length of the Longest Common Prefix
// https://leetcode.com/problems/find-the-length-of-the-longest-common-prefix/

#include <stdlib.h>
#include <stdbool.h>
#include <stdio.h>
#include <string.h>

typedef struct { int key; bool used; } HEnt;

static unsigned hash_u(unsigned x) { x ^= x >> 16; x *= 0x7feb352dU; x ^= x >> 15; x *= 0x846ca68bU; x ^= x >> 16; return x; }

static void hput(HEnt* t, int cap, int key) {
    unsigned h = hash_u((unsigned)key) & (unsigned)(cap - 1);
    while (t[h].used) {
        if (t[h].key == key) return;
        h = (h + 1) & (unsigned)(cap - 1);
    }
    t[h].used = true; t[h].key = key;
}
static bool hhas(HEnt* t, int cap, int key) {
    unsigned h = hash_u((unsigned)key) & (unsigned)(cap - 1);
    while (t[h].used) {
        if (t[h].key == key) return true;
        h = (h + 1) & (unsigned)(cap - 1);
    }
    return false;
}

int longestCommonPrefix(int* arr1, int arr1Size, int* arr2, int arr2Size) {
    int cap = 1;
    while (cap < arr1Size * 20 + 16) cap <<= 1;
    HEnt* t = (HEnt*)calloc((size_t)cap, sizeof(HEnt));
    for (int i = 0; i < arr1Size; i++) {
        for (int x = arr1[i]; x > 0; x /= 10) hput(t, cap, x);
    }
    int mx = 0;
    for (int i = 0; i < arr2Size; i++) {
        for (int x = arr2[i]; x > 0; x /= 10) {
            if (hhas(t, cap, x)) { if (x > mx) mx = x; break; }
        }
    }
    free(t);
    if (mx == 0) return 0;
    char buf[16];
    sprintf(buf, "%d", mx);
    return (int)strlen(buf);
}
