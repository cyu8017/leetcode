// LeetCode 3890 - Integers With Multiple Sum Of Two Cubes
// https://leetcode.com/problems/integers-with-multiple-sum-of-two-cubes/

#include <stdlib.h>
#include <string.h>

static int* GOOD3890;
static int GOODN3890;
static int ready3890 = 0;

static int cmpInt3890(const void* a, const void* b) {
    int x = *(const int*)a, y = *(const int*)b;
    return (x > y) - (x < y);
}

static void init3890(void) {
    if (ready3890) return;
    const int LIMIT = 1000000000;
    /* hash map for counts - use simple open addressing */
    enum { HS = 1 << 20 };
    typedef struct { int key, val, used; } Ent;
    Ent* cnt = calloc(HS, sizeof(Ent));
    int cubes[1001];
    for (int i = 0; i <= 1000; i++) cubes[i] = i * i * i;
    for (int a = 1; a <= 1000; a++) {
        for (int b = a; b <= 1000; b++) {
            int x = cubes[a] + cubes[b];
            if (x > LIMIT || x < 0) break;
            unsigned h = (unsigned)x % HS;
            for (;;) {
                if (!cnt[h].used) { cnt[h].used = 1; cnt[h].key = x; cnt[h].val = 1; break; }
                if (cnt[h].key == x) { cnt[h].val++; break; }
                h = (h + 1) % HS;
            }
        }
    }
    int cap = 1024;
    GOOD3890 = malloc((size_t)cap * sizeof(int));
    GOODN3890 = 0;
    for (int i = 0; i < HS; i++) {
        if (cnt[i].used && cnt[i].val > 1) {
            if (GOODN3890 == cap) {
                cap *= 2;
                GOOD3890 = realloc(GOOD3890, (size_t)cap * sizeof(int));
            }
            GOOD3890[GOODN3890++] = cnt[i].key;
        }
    }
    free(cnt);
    qsort(GOOD3890, (size_t)GOODN3890, sizeof(int), cmpInt3890);
    ready3890 = 1;
}

int* findGoodIntegers(int n, int* returnSize) {
    init3890();
    int lo = 0, hi = GOODN3890;
    while (lo < hi) {
        int mid = (lo + hi) / 2;
        if (GOOD3890[mid] > n) hi = mid;
        else lo = mid + 1;
    }
    int* ans = malloc((size_t)lo * sizeof(int));
    memcpy(ans, GOOD3890, (size_t)lo * sizeof(int));
    *returnSize = lo;
    return ans;
}
