// LeetCode 2605 - Form Smallest Number From Two Digit Arrays
// https://leetcode.com/problems/form-smallest-number-from-two-digit-arrays/

#include <stdbool.h>
#include <string.h>

int minNumber(int* nums1, int nums1Size, int* nums2, int nums2Size) {
    bool s1[10] = {0}, s2[10] = {0};
    for (int i = 0; i < nums1Size; i++) s1[nums1[i]] = true;
    for (int i = 0; i < nums2Size; i++) s2[nums2[i]] = true;
    int bestShared = 10;
    for (int d = 1; d <= 9; d++) if (s1[d] && s2[d] && d < bestShared) bestShared = d;
    if (bestShared < 10) return bestShared;
    int m1 = 10, m2 = 10;
    for (int i = 0; i < nums1Size; i++) if (nums1[i] < m1) m1 = nums1[i];
    for (int i = 0; i < nums2Size; i++) if (nums2[i] < m2) m2 = nums2[i];
    if (m1 < m2) return m1 * 10 + m2;
    return m2 * 10 + m1;
}
