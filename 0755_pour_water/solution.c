// LeetCode 0755 - Pour Water
#include <stdlib.h>

int* pourWater(int* heights, int heightsSize, int volume, int k, int* returnSize) {
    for (int v = 0; v < volume; v++) {
        int index = k;
        for (int i = k - 1; i >= 0; i--) {
            if (heights[i] > heights[index]) break;
            if (heights[i] < heights[index]) index = i;
        }
        if (index != k) { heights[index]++; continue; }
        index = k;
        for (int i = k + 1; i < heightsSize; i++) {
            if (heights[i] > heights[index]) break;
            if (heights[i] < heights[index]) index = i;
        }
        heights[index]++;
    }
    int* result = (int*)malloc((size_t)heightsSize * sizeof(int));
    for (int i = 0; i < heightsSize; i++) result[i] = heights[i];
    *returnSize = heightsSize;
    return result;
}
