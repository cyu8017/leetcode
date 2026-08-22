// LeetCode 3477 - Fruits Into Baskets II
// https://leetcode.com/problems/fruits-into-baskets-ii/

#include <stdlib.h>
#include <string.h>

int numOfUnplacedFruits(int* fruits, int fruitsSize, int* baskets, int basketsSize) {
    int* used = (int*)calloc((size_t)basketsSize, sizeof(int));
    int unplaced = 0;
    for (int i = 0; i < fruitsSize; i++) {
        int placed = 0;
        for (int j = 0; j < basketsSize; j++) {
            if (!used[j] && baskets[j] >= fruits[i]) {
                used[j] = 1;
                placed = 1;
                break;
            }
        }
        if (!placed) unplaced++;
    }
    free(used);
    return unplaced;
}
