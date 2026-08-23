// LeetCode 3115 - Maximum Prime Difference
// https://leetcode.com/problems/maximum-prime-difference/

public class Solution {
    static bool IsPrime(int n) {
        if (n < 2) return false;
        for (int i = 2; i <= n / i; i++)
            if (n % i == 0) return false;
        return true;
    }

    public int MaximumPrimeDifference(int[] nums) {
        for (int i = 0; ; i++) {
            if (IsPrime(nums[i])) {
                for (int j = nums.Length - 1; ; j--) {
                    if (IsPrime(nums[j])) return j - i;
                }
            }
        }
    }
}
