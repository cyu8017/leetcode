// LeetCode 1874 - Minimize Product Sum of Two Arrays
// https://leetcode.com/problems/minimize-product-sum-of-two-arrays/

public class Solution {
    public int MinProductSum(int[] nums1, int[] nums2) {
        Array.Sort(nums1);
        Array.Sort(nums2);
        int answer = 0;
        for (int i = 0; i < nums1.Length; i++) {
            answer += nums1[i] * nums2[nums2.Length - 1 - i];
        }
        return answer;
    }
}
