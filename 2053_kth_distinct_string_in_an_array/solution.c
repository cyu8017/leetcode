// LeetCode 2053 - Kth Distinct String in an Array
// https://leetcode.com/problems/kth-distinct-string-in-an-array/

#include <stdlib.h>
#include <string.h>

char* kthDistinct(char** arr, int arrSize, int k) {
    for (int i = 0; i < arrSize; i++) {
        int c = 0;
        for (int j = 0; j < arrSize; j++) if (strcmp(arr[i], arr[j]) == 0) c++;
        if (c == 1) {
            k--;
            if (k == 0) return arr[i];
        }
    }
    return "";
}
