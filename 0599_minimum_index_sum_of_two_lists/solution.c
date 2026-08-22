// LeetCode 0599 - Minimum Index Sum of Two Lists
// https://leetcode.com/problems/minimum-index-sum-of-two-lists/

#include <limits.h>
#include <stdlib.h>
#include <string.h>

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
char** findRestaurant(char** list1, int list1Size, char** list2, int list2Size, int* returnSize) {
    int best = INT_MAX;
    int capacity = list1Size < list2Size ? list1Size : list2Size;
    char** answer = (char**)malloc((size_t)capacity * sizeof(char*));
    int count = 0;
    for (int j = 0; j < list2Size; j++) {
        for (int i = 0; i < list1Size; i++) {
            if (strcmp(list1[i], list2[j]) == 0) {
                int total = i + j;
                if (total < best) {
                    best = total;
                    count = 0;
                    answer[count++] = list2[j];
                } else if (total == best) {
                    answer[count++] = list2[j];
                }
                break;
            }
        }
    }
    *returnSize = count;
    return answer;
}
