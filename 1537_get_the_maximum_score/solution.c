// LeetCode 1537 - Get the Maximum Score
// https://leetcode.com/problems/get-the-maximum-score/

int maxSum(int* nums1, int nums1Size, int* nums2, int nums2Size) {
    int i = 0, j = 0;
    long long first = 0, second = 0;
    while (i < nums1Size || j < nums2Size) {
        if (j == nums2Size || (i < nums1Size && nums1[i] < nums2[j])) {
            first += nums1[i++];
        } else if (i == nums1Size || nums2[j] < nums1[i]) {
            second += nums2[j++];
        } else {
            first = second = (first > second ? first : second) + nums1[i];
            i++;
            j++;
        }
    }
    long long ans = first > second ? first : second;
    return (int)(ans % 1000000007LL);
}
