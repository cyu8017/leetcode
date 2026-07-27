// LeetCode 1652 - Defuse the Bomb
// https://leetcode.com/problems/defuse-the-bomb/

class Solution {
    public int[] decrypt(int[] code, int k) {
        int n = code.length;
        int[] ans = new int[n];
        if (k == 0) {
            return ans;
        }
        int[] doubled = new int[n * 2];
        for (int i = 0; i < n; i++) {
            doubled[i] = code[i];
            doubled[i + n] = code[i];
        }
        for (int i = 0; i < n; i++) {
            int sum = 0;
            if (k > 0) {
                for (int j = i + 1; j <= i + k; j++) {
                    sum += doubled[j];
                }
            } else {
                for (int j = i + n + k; j < i + n; j++) {
                    sum += doubled[j];
                }
            }
            ans[i] = sum;
        }
        return ans;
    }
}
