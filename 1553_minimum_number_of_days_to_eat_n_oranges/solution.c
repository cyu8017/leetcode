// LeetCode 1553 - Minimum Number of Days to Eat N Oranges
// https://leetcode.com/problems/minimum-number-of-days-to-eat-n-oranges/

#include <stdlib.h>

typedef struct {
    int key;
    int val;
    int used;
} Entry1553;

static Entry1553* table1553;
static int cap1553;

static int get1553(int key, int* found) {
    unsigned h = (unsigned)key % (unsigned)cap1553;
    while (table1553[h].used) {
        if (table1553[h].key == key) {
            *found = 1;
            return table1553[h].val;
        }
        h = (h + 1) % (unsigned)cap1553;
    }
    *found = 0;
    return 0;
}

static void put1553(int key, int val) {
    unsigned h = (unsigned)key % (unsigned)cap1553;
    while (table1553[h].used && table1553[h].key != key) h = (h + 1) % (unsigned)cap1553;
    table1553[h].used = 1;
    table1553[h].key = key;
    table1553[h].val = val;
}

static int dp1553(int x) {
    if (x <= 1) return x;
    int found, cached = get1553(x, &found);
    if (found) return cached;
    int a = x % 2 + dp1553(x / 2);
    int b = x % 3 + dp1553(x / 3);
    int ans = 1 + (a < b ? a : b);
    put1553(x, ans);
    return ans;
}

int minDays(int n) {
    cap1553 = 1;
    while (cap1553 < 200000) cap1553 <<= 1;
    table1553 = (Entry1553*)calloc((size_t)cap1553, sizeof(Entry1553));
    int ans = dp1553(n);
    free(table1553);
    return ans;
}
