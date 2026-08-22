// LeetCode 3162 - Find the Number of Good Pairs I
// https://leetcode.com/problems/find-the-number-of-good-pairs-i/

int numberOfPairs(int* nums1, int nums1Size, int* nums2, int nums2Size, int k) {
    int ans = 0;
    for (int i = 0; i < nums1Size; i++)
        for (int j = 0; j < nums2Size; j++)
            if (nums1[i] % (nums2[j] * k) == 0) ans++;
    return ans;
}
