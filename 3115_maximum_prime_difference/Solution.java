// LeetCode 3115 - Maximum Prime Difference
// https://leetcode.com/problems/maximum-prime-difference/

class Solution {
    private boolean isPrime(int n) {
        if (n < 2) return false;
        for (int i = 2; i <= n / i; i++)
            if (n % i == 0) return false;
        return true;
    }

    public int maximumPrimeDifference(int[] nums) {
        for (int i = 0; ; i++) {
            if (isPrime(nums[i])) {
                for (int j = nums.length - 1; ; j--) {
                    if (isPrime(nums[j])) return j - i;
                }
            }
        }
    }
}
