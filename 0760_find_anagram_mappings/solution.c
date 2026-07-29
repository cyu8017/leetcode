// LeetCode 0760 - Find Anagram Mappings
// https://leetcode.com/problems/find-anagram-mappings/

#include <stdlib.h>

int* anagramMappings(int* nums1, int nums1Size, int* nums2, int nums2Size, int* returnSize) {
    (void)nums2Size;
    int* result = (int*)malloc((size_t)nums1Size * sizeof(int));
    char* used = (char*)calloc((size_t)nums1Size, 1);
    for (int i = 0; i < nums1Size; i++) {
        for (int j = 0; j < nums1Size; j++) {
            if (!used[j] && nums2[j] == nums1[i]) {
                result[i] = j;
                used[j] = 1;
                break;
            }
        }
    }
    free(used);
    *returnSize = nums1Size;
    return result;
}
