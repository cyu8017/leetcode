// LeetCode 0492 - Construct the Rectangle
// https://leetcode.com/problems/construct-the-rectangle/

#include <math.h>
#include <stdlib.h>

int* constructRectangle(int area, int* returnSize) {
    int* result = (int*)malloc(2 * sizeof(int));
    const int limit = (int)sqrt((double)area);
    for (int width = limit; width > 0; width--) {
        if (area % width == 0) {
            result[0] = area / width;
            result[1] = width;
            *returnSize = 2;
            return result;
        }
    }
    result[0] = area;
    result[1] = 1;
    *returnSize = 2;
    return result;
}
