// LeetCode 1588 - Sum of All Odd Length Subarrays
// https://leetcode.com/problems/sum-of-all-odd-length-subarrays/

public class Solution {
    public int SumOddLengthSubarrays(int[] arr) {
        int n = arr.Length, ans = 0;
        for (int i = 0; i < n; i++)
            ans += arr[i] * (((i + 1) * (n - i) + 1) / 2);
        return ans;
    }
}
