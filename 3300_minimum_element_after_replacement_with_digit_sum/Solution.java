// LeetCode 3300 - Minimum Element After Replacement With Digit Sum
// https://leetcode.com/problems/minimum-element-after-replacement-with-digit-sum/

class Solution {
    public int minElement(int[] nums) {
        int ans = 1000000000;
        for (int num : nums) {
            int x = num, s = 0;
            while (x > 0) { s += x % 10; x /= 10; }
            if (s < ans) ans = s;
        }
        return ans;
    }
}
