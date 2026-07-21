// LeetCode 1855 - Maximum Distance Between a Pair of Values
// https://leetcode.com/problems/maximum-distance-between-a-pair-of-values/

int maxDistance(int* nums1, int nums1Size, int* nums2, int nums2Size) {
    int answer = 0;
    int j = 0;
    for (int i = 0; i < nums1Size; i++) {
        while (j < nums2Size && nums1[i] <= nums2[j]) j++;
        int dist = j - i - 1;
        if (dist > answer) answer = dist;
    }
    return answer;
}
