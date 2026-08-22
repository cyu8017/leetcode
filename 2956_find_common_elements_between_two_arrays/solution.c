// LeetCode 2956 - Find Common Elements Between Two Arrays
// https://leetcode.com/problems/find-common-elements-between-two-arrays/

#include <stdlib.h>
#include <stdbool.h>
#include <string.h>

int* findIntersectionValues(int* nums1, int nums1Size, int* nums2, int nums2Size, int* returnSize) {
    bool s1[101] = {false}, s2[101] = {false};
    for (int i = 0; i < nums1Size; i++) s1[nums1[i]] = true;
    for (int i = 0; i < nums2Size; i++) s2[nums2[i]] = true;
    int a = 0, b = 0;
    for (int i = 0; i < nums1Size; i++) if (s2[nums1[i]]) a++;
    for (int i = 0; i < nums2Size; i++) if (s1[nums2[i]]) b++;
    int* ans = (int*)malloc(2 * sizeof(int));
    ans[0] = a; ans[1] = b;
    *returnSize = 2;
    return ans;
}
