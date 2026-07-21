// LeetCode 1893 - Check if All the Integers in a Range Are Covered
// https://leetcode.com/problems/check-if-all-the-integers-in-a-range-are-covered/

#include <stdbool.h>

bool isCovered(int** ranges, int rangesSize, int* rangesColSize, int left, int right) {
    (void)rangesColSize;
    bool covered[51] = {false};
    for (int i = 0; i < rangesSize; i++) {
        for (int v = ranges[i][0]; v <= ranges[i][1]; v++) covered[v] = true;
    }
    for (int v = left; v <= right; v++) {
        if (!covered[v]) return false;
    }
    return true;
}
