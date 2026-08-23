// LeetCode 3895 - Count Digit Appearances
// https://leetcode.com/problems/count-digit-appearances/

class Solution {
    public int countDigitOccurrences(int[] nums, int digit) {
        int ans = 0;
        for (int num : nums) {
            int x = num;
            for (; x > 0; x /= 10) {
                if (x % 10 == digit) ans++;
            }
        }
        return ans;
    }
}
