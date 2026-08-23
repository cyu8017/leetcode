// LeetCode 3895 - Count Digit Appearances
// https://leetcode.com/problems/count-digit-appearances/

public class Solution {
    public int CountDigitOccurrences(int[] nums, int digit) {
        int ans = 0;
        foreach (int num in nums) {
            int x = num;
            for (; x > 0; x /= 10) {
                if (x % 10 == digit) ans++;
            }
        }
        return ans;
    }
}
