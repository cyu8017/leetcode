// LeetCode 1652 - Defuse the Bomb
// https://leetcode.com/problems/defuse-the-bomb/

public class Solution {
    public int[] Decrypt(int[] code, int k) {
        int n = code.Length;
        var ans = new int[n];
        if (k == 0) return ans;
        for (int i = 0; i < n; i++) {
            int sum = 0;
            if (k > 0) {
                for (int j = 1; j <= k; j++) sum += code[(i + j) % n];
            } else {
                for (int j = 1; j <= -k; j++) sum += code[(i - j + n) % n];
            }
            ans[i] = sum;
        }
        return ans;
    }
}
