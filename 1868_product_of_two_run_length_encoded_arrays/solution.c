// LeetCode 1868 - Product of Two Run-Length Encoded Arrays
// https://leetcode.com/problems/product-of-two-run-length-encoded-arrays/

#include <stdlib.h>

/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *returnColumnSizes array must be malloced, assume caller calls free().
 */
int** findRLEArray(int** encoded1, int encoded1Size, int* encoded1ColSize, int** encoded2,
                   int encoded2Size, int* encoded2ColSize, int* returnSize,
                   int** returnColumnSizes) {
    (void)encoded1ColSize;
    (void)encoded2ColSize;
    int cap = encoded1Size + encoded2Size;
    int** result = (int**)malloc((size_t)cap * sizeof(int*));
    int count = 0;
    int i = 0, j = 0;
    int rem1 = encoded1[0][1];
    int rem2 = encoded2[0][1];
    while (i < encoded1Size) {
        int take = rem1 < rem2 ? rem1 : rem2;
        int value = encoded1[i][0] * encoded2[j][0];
        if (count > 0 && result[count - 1][0] == value) {
            result[count - 1][1] += take;
        } else {
            result[count] = (int*)malloc(2 * sizeof(int));
            result[count][0] = value;
            result[count][1] = take;
            count++;
        }
        rem1 -= take;
        rem2 -= take;
        if (rem1 == 0) {
            i++;
            if (i < encoded1Size) rem1 = encoded1[i][1];
        }
        if (rem2 == 0) {
            j++;
            if (j < encoded2Size) rem2 = encoded2[j][1];
        }
    }
    *returnColumnSizes = (int*)malloc((size_t)count * sizeof(int));
    for (int t = 0; t < count; t++) (*returnColumnSizes)[t] = 2;
    *returnSize = count;
    return result;
}
