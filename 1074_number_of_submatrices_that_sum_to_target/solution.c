// LeetCode 1074 - Number of Submatrices That Sum to Target
// https://leetcode.com/problems/number-of-submatrices-that-sum-to-target/

#include <stdlib.h>

typedef struct {
    int key;
    int count;
    int used;
} HashEntry;

static int hashFindAdd(HashEntry* table, int slots, int key, int delta, int* outCount) {
    unsigned h = (unsigned)key * 2654435761u;
    int idx = (int)(h % (unsigned)slots);
    for (int probes = 0; probes < slots; probes++) {
        if (!table[idx].used) {
            if (delta > 0) {
                table[idx].used = 1;
                table[idx].key = key;
                table[idx].count = delta;
            }
            *outCount = 0;
            return 0;
        }
        if (table[idx].key == key) {
            *outCount = table[idx].count;
            table[idx].count += delta;
            return *outCount;
        }
        idx = (idx + 1) % slots;
    }
    *outCount = 0;
    return 0;
}

int numSubmatrixSumTarget(int** matrix, int matrixSize, int* matrixColSize, int target) {
    int rows = matrixSize;
    int cols = matrixColSize[0];
    int ans = 0;
    int* rowSum = (int*)malloc((size_t)rows * sizeof(int));
    int slots = rows * 4 + 17;
    HashEntry* table = (HashEntry*)malloc((size_t)slots * sizeof(HashEntry));
    for (int left = 0; left < cols; left++) {
        for (int r = 0; r < rows; r++) {
            rowSum[r] = 0;
        }
        for (int right = left; right < cols; right++) {
            for (int r = 0; r < rows; r++) {
                rowSum[r] += matrix[r][right];
            }
            for (int i = 0; i < slots; i++) {
                table[i].used = 0;
                table[i].count = 0;
            }
            // seed 0 -> 1
            int dummy;
            hashFindAdd(table, slots, 0, 1, &dummy);
            int prefix = 0;
            for (int r = 0; r < rows; r++) {
                prefix += rowSum[r];
                int seen;
                hashFindAdd(table, slots, prefix - target, 0, &seen);
                ans += seen;
                hashFindAdd(table, slots, prefix, 1, &dummy);
            }
        }
    }
    free(rowSum);
    free(table);
    return ans;
}
