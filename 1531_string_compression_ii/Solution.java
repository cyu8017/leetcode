// LeetCode 1531 - String Compression II
// https://leetcode.com/problems/string-compression-ii/

class Solution {
    private String s;
    private int[][] memo;

    public int getLengthOfOptimalCompression(String s, int k) {
        this.s = s;
        memo = new int[s.length() + 1][k + 1];
        for (int[] row : memo) {
            for (int j = 0; j < row.length; j++) {
                row[j] = -1;
            }
        }
        return dp(0, k);
    }

    private int dp(int index, int remaining) {
        if (remaining < 0) {
            return 1_000_000_000;
        }
        if (index == s.length() || s.length() - index <= remaining) {
            return 0;
        }
        if (memo[index][remaining] != -1) {
            return memo[index][remaining];
        }
        int answer = dp(index + 1, remaining - 1);
        int same = 0;
        int removed = 0;
        for (int j = index; j < s.length(); j++) {
            if (s.charAt(j) == s.charAt(index)) {
                same++;
                int encoded = 1 + (same >= 2 ? 1 : 0) + (same >= 10 ? 1 : 0) + (same >= 100 ? 1 : 0);
                answer = Math.min(answer, encoded + dp(j + 1, remaining - removed));
            } else {
                removed++;
                if (removed > remaining) {
                    break;
                }
            }
        }
        memo[index][remaining] = answer;
        return answer;
    }
}
