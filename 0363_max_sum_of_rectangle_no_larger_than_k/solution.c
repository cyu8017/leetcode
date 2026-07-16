// LeetCode 0363 - Max Sum of Rectangle No Larger Than K
// https://leetcode.com/problems/max-sum-of-rectangle-no-larger-than-k/

#include <limits.h>
#include <stdlib.h>

static int lowerBound(int* values, int count, int target) {
    int left = 0;
    int right = count;
    while (left < right) {
        int mid = left + (right - left) / 2;
        if (values[mid] < target) {
            left = mid + 1;
        } else {
            right = mid;
        }
    }
    return left;
}

static void insertSorted(int** values, int* count, int* capacity, int value) {
    int index = lowerBound(*values, *count, value);
    if (*count >= *capacity) {
        *capacity = *capacity == 0 ? 8 : *capacity * 2;
        *values = (int*)realloc(*values, (size_t)(*capacity) * sizeof(int));
    }
    for (int shift = *count; shift > index; shift--) {
        (*values)[shift] = (*values)[shift - 1];
    }
    (*values)[index] = value;
    *count += 1;
}

int maxSumSubmatrix(int** matrix, int matrixSize, int* matrixColSize, int k) {
    if (matrixSize == 0) {
        return 0;
    }

    int rows = matrixSize;
    int cols = matrixColSize[0];
    int result = INT_MIN;
    int* colSums = (int*)calloc((size_t)cols, sizeof(int));

    for (int top = 0; top < rows; top++) {
        for (int col = 0; col < cols; col++) {
            colSums[col] = 0;
        }

        for (int bottom = top; bottom < rows; bottom++) {
            int* prefixSums = NULL;
            int prefixCount = 0;
            int prefixCapacity = 0;
            insertSorted(&prefixSums, &prefixCount, &prefixCapacity, 0);
            int running = 0;

            for (int col = 0; col < cols; col++) {
                colSums[col] += matrix[bottom][col];
                running += colSums[col];

                int index = lowerBound(prefixSums, prefixCount, running - k);
                if (index < prefixCount) {
                    int candidate = running - prefixSums[index];
                    if (candidate > result) {
                        result = candidate;
                    }
                }

                insertSorted(&prefixSums, &prefixCount, &prefixCapacity, running);
            }

            free(prefixSums);
        }
    }

    free(colSums);
    return result;
}
