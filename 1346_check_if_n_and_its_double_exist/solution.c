// LeetCode 1346 - Check If N and Its Double Exist
// https://leetcode.com/problems/check-if-n-and-its-double-exist/

#include <stdbool.h>
#include <stdlib.h>

bool checkIfExist(int* arr, int arrSize) {
    // simple set via sorted unique scan - use hash with open array
    int* seen = (int*)malloc(arrSize * sizeof(int));
    int sn = 0;
    for (int i = 0; i < arrSize; i++) {
        int value = arr[i];
        for (int j = 0; j < sn; j++) {
            if (seen[j] == 2 * value || (value % 2 == 0 && seen[j] == value / 2)) {
                free(seen);
                return true;
            }
        }
        seen[sn++] = value;
    }
    free(seen);
    return false;
}
