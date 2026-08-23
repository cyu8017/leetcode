// LeetCode 2098 - Subsequence of Size K With the Largest Even Sum
// https://leetcode.com/problems/subsequence-of-size-k-with-the-largest-even-sum/

public class Solution {
    public long LargestEvenSum(int[] nums, int k) {
        Array.Sort(nums, (a, b) => b.CompareTo(a));
        long sum = 0;
        for (int i = 0; i < k; i++) sum += nums[i];
        if (sum % 2 == 0) return sum;
        long ans = -1;
        int oddIn = -1, evenIn = -1, oddOut = -1, evenOut = -1;
        for (int i = k - 1; i >= 0; i--) {
            if (nums[i] % 2 != 0 && oddIn == -1) oddIn = i;
            if (nums[i] % 2 == 0 && evenIn == -1) evenIn = i;
        }
        for (int i = k; i < nums.Length; i++) {
            if (nums[i] % 2 != 0 && oddOut == -1) oddOut = i;
            if (nums[i] % 2 == 0 && evenOut == -1) evenOut = i;
        }
        if (oddIn != -1 && evenOut != -1) ans = Math.Max(ans, sum - nums[oddIn] + nums[evenOut]);
        if (evenIn != -1 && oddOut != -1) ans = Math.Max(ans, sum - nums[evenIn] + nums[oddOut]);
        return ans;
    }
}
