// LeetCode 1375 - Number Of Times Binary String Is Prefix Aligned
// https://leetcode.com/problems/number-of-times-binary-string-is-prefix-aligned/

public class Solution {
    public int NumTimesAllBlue(int[] flips) {
        int ans = 0, mx = 0;
        for (int i = 0; i < flips.Length; i++) {
            mx = System.Math.Max(mx, flips[i]);
            if (mx == i + 1) ans++;
        }
        return ans;
    }
}
