// LeetCode 3300 - Minimum Element After Replacement With Digit Sum
// https://leetcode.com/problems/minimum-element-after-replacement-with-digit-sum/

public class Solution {
    public int MinElement(int[] nums) {
        int ans = 1000000000;
        foreach (int num in nums) {
            int x = num, s = 0;
            while (x > 0) { s += x % 10; x /= 10; }
            if (s < ans) ans = s;
        }
        return ans;
    }
}
