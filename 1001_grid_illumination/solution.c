// LeetCode 1001 - Grid Illumination
// https://leetcode.com/problems/grid-illumination/

#include <stdlib.h>
#include <string.h>

typedef struct {
    long long key;
    int count;
    int state; /* 0 empty, 1 occupied, 2 tombstone */
} HashEntry;

typedef struct {
    long long key;
    int state;
} SetEntry;

static unsigned hash_ll(long long key, int cap) {
    unsigned long long x = (unsigned long long)key;
    x ^= x >> 33;
    x *= 0xff51afd7ed558ccdULL;
    x ^= x >> 33;
    return (unsigned)(x % (unsigned)cap);
}

static void hash_add(HashEntry* table, int cap, long long key, int delta) {
    unsigned h = hash_ll(key, cap);
    int firstTomb = -1;
    while (table[h].state != 0) {
        if (table[h].state == 2 && firstTomb < 0) firstTomb = (int)h;
        if (table[h].state == 1 && table[h].key == key) {
            table[h].count += delta;
            return;
        }
        h = (h + 1) % (unsigned)cap;
    }
    unsigned slot = firstTomb >= 0 ? (unsigned)firstTomb : h;
    table[slot].state = 1;
    table[slot].key = key;
    table[slot].count = delta;
}

static int hash_get(HashEntry* table, int cap, long long key) {
    unsigned h = hash_ll(key, cap);
    while (table[h].state != 0) {
        if (table[h].state == 1 && table[h].key == key) return table[h].count;
        h = (h + 1) % (unsigned)cap;
    }
    return 0;
}

static void set_add(SetEntry* table, int cap, long long key) {
    unsigned h = hash_ll(key, cap);
    int firstTomb = -1;
    while (table[h].state != 0) {
        if (table[h].state == 2 && firstTomb < 0) firstTomb = (int)h;
        if (table[h].state == 1 && table[h].key == key) return;
        h = (h + 1) % (unsigned)cap;
    }
    unsigned slot = firstTomb >= 0 ? (unsigned)firstTomb : h;
    table[slot].state = 1;
    table[slot].key = key;
}

static int set_has(SetEntry* table, int cap, long long key) {
    unsigned h = hash_ll(key, cap);
    while (table[h].state != 0) {
        if (table[h].state == 1 && table[h].key == key) return 1;
        h = (h + 1) % (unsigned)cap;
    }
    return 0;
}

static void set_remove(SetEntry* table, int cap, long long key) {
    unsigned h = hash_ll(key, cap);
    while (table[h].state != 0) {
        if (table[h].state == 1 && table[h].key == key) {
            table[h].state = 2;
            return;
        }
        h = (h + 1) % (unsigned)cap;
    }
}

static long long pack(int r, int c) {
    return ((long long)r << 32) | (unsigned)c;
}

int* gridIllumination(int n, int** lamps, int lampsSize, int* lampsColSize,
                      int** queries, int queriesSize, int* queriesColSize, int* returnSize) {
    (void)n;
    (void)lampsColSize;
    (void)queriesColSize;
    int cap = (lampsSize + queriesSize + 16) * 8 + 64;
    HashEntry* rows = (HashEntry*)calloc((size_t)cap, sizeof(HashEntry));
    HashEntry* cols = (HashEntry*)calloc((size_t)cap, sizeof(HashEntry));
    HashEntry* diag1 = (HashEntry*)calloc((size_t)cap, sizeof(HashEntry));
    HashEntry* diag2 = (HashEntry*)calloc((size_t)cap, sizeof(HashEntry));
    SetEntry* lit = (SetEntry*)calloc((size_t)cap, sizeof(SetEntry));

    for (int i = 0; i < lampsSize; i++) {
        int r = lamps[i][0], c = lamps[i][1];
        long long key = pack(r, c);
        if (set_has(lit, cap, key)) continue;
        set_add(lit, cap, key);
        hash_add(rows, cap, r, 1);
        hash_add(cols, cap, c, 1);
        hash_add(diag1, cap, (long long)r - c, 1);
        hash_add(diag2, cap, (long long)r + c, 1);
    }

    int* ans = (int*)malloc((size_t)queriesSize * sizeof(int));
    *returnSize = queriesSize;
    for (int q = 0; q < queriesSize; q++) {
        int r = queries[q][0], c = queries[q][1];
        ans[q] = (hash_get(rows, cap, r) || hash_get(cols, cap, c) ||
                  hash_get(diag1, cap, (long long)r - c) ||
                  hash_get(diag2, cap, (long long)r + c))
                     ? 1
                     : 0;
        for (int i = r - 1; i <= r + 1; i++) {
            for (int j = c - 1; j <= c + 1; j++) {
                long long key = pack(i, j);
                if (!set_has(lit, cap, key)) continue;
                set_remove(lit, cap, key);
                hash_add(rows, cap, i, -1);
                hash_add(cols, cap, j, -1);
                hash_add(diag1, cap, (long long)i - j, -1);
                hash_add(diag2, cap, (long long)i + j, -1);
            }
        }
    }
    free(rows);
    free(cols);
    free(diag1);
    free(diag2);
    free(lit);
    return ans;
}
