// LeetCode 1088 - Confusing Number II
// https://leetcode.com/problems/confusing-number-ii/

class Solution {
    private int ans;
    private int n;
    private final int[] rotate = new int[] { 0, 1, -1, -1, -1, -1, 9, -1, 8, 6 };
    private final int[] digits = new int[] { 0, 1, 6, 8, 9 };

    public int confusingNumberII(int n) {
        this.n = n;
        this.ans = 0;
        dfs(0);
        return ans;
    }

    private boolean isConfusing(int num) {
        int original = num;
        int rotated = 0;
        while (num > 0) {
            int d = num % 10;
            rotated = rotated * 10 + rotate[d];
            num /= 10;
        }
        return rotated != original;
    }

    private void dfs(long cur) {
        if (cur > n) {
            return;
        }
        if (cur != 0 && isConfusing((int) cur)) {
            ans++;
        }
        if (cur == 0) {
            for (int d : new int[] { 1, 6, 8, 9 }) {
                dfs(d);
            }
        } else {
            for (int d : digits) {
                dfs(cur * 10 + d);
            }
        }
    }
}
