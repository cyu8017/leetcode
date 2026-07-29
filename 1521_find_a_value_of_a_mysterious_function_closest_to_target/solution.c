// LeetCode 1521 - Find a Value of a Mysterious Function Closest to Target
// https://leetcode.com/problems/find-a-value-of-a-mysterious-function-closest-to-target/

#include <stdlib.h>

int closestToTarget(int* arr, int arrSize, int target) {
    int* current = (int*)malloc((size_t)arrSize * sizeof(int));
    int curSize = 0;
    int answer = abs(arr[0] - target);
    for (int i = 0; i < arrSize; i++) {
        int value = arr[i];
        int* next = (int*)malloc((size_t)(curSize + 1) * sizeof(int));
        int nextSize = 0;
        next[nextSize++] = value;
        for (int j = 0; j < curSize; j++) {
            int cand = value & current[j];
            int found = 0;
            for (int k = 0; k < nextSize; k++) if (next[k] == cand) { found = 1; break; }
            if (!found) next[nextSize++] = cand;
        }
        free(current);
        current = next;
        curSize = nextSize;
        for (int j = 0; j < curSize; j++) {
            int d = abs(current[j] - target);
            if (d < answer) answer = d;
        }
    }
    free(current);
    return answer;
}
