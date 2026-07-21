// LeetCode 1899 - Merge Triplets to Form Target Triplet
// https://leetcode.com/problems/merge-triplets-to-form-target-triplet/

#include <stdbool.h>

bool mergeTriplets(int** triplets, int tripletsSize, int* tripletsColSize, int* target,
                   int targetSize) {
    (void)tripletsColSize;
    (void)targetSize;
    int merged[3] = {0, 0, 0};
    for (int i = 0; i < tripletsSize; i++) {
        int a = triplets[i][0], b = triplets[i][1], c = triplets[i][2];
        if (a <= target[0] && b <= target[1] && c <= target[2]) {
            if (a > merged[0]) merged[0] = a;
            if (b > merged[1]) merged[1] = b;
            if (c > merged[2]) merged[2] = c;
        }
    }
    return merged[0] == target[0] && merged[1] == target[1] && merged[2] == target[2];
}
