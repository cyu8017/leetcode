// LeetCode 1088 - Confusing Number II
// https://leetcode.com/problems/confusing-number-ii/

using System.Collections.Generic;

public class Solution {
    public int ConfusingNumberII(int n) {
        var rotate = new Dictionary<int, int> {
            [0] = 0, [1] = 1, [6] = 9, [8] = 8, [9] = 6
        };
        int[] digits = { 0, 1, 6, 8, 9 };
        int ans = 0;

        bool IsConfusing(int num) {
            int original = num;
            int rotated = 0;
            while (num > 0) {
                int d = num % 10;
                rotated = rotated * 10 + rotate[d];
                num /= 10;
            }
            return rotated != original;
        }

        void Dfs(long cur) {
            if (cur > n) {
                return;
            }
            if (cur > 0 && IsConfusing((int)cur)) {
                ans++;
            }
            if (cur == 0) {
                foreach (int d in new[] { 1, 6, 8, 9 }) {
                    Dfs(d);
                }
            } else {
                foreach (int d in digits) {
                    Dfs(cur * 10 + d);
                }
            }
        }

        Dfs(0);
        return ans;
    }
}
