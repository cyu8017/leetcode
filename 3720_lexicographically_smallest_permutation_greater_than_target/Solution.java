// LeetCode 3720 - Lexicographically Smallest Permutation Greater Than Target
// https://leetcode.com/problems/lexicographically_smallest_permutation_greater_than_target/

class Solution {
    private int[] cnt;
    private char[] ans;
    private String target;
    private int n;

    public String lexGreaterPermutation(String s, String target) {
        cnt = new int[26];
        for (char c : s.toCharArray()) cnt[c - 'a']++;
        n = s.length();
        this.target = target;
        ans = new char[n];
        if (dfs(0, false)) return new String(ans);
        return "";
    }

    private boolean dfs(int pos, boolean greater) {
        if (pos == n) return greater;
        int start = greater ? 0 : (target.charAt(pos) - 'a');
        for (int c = start; c < 26; c++) {
            if (cnt[c] == 0) continue;
            cnt[c]--;
            ans[pos] = (char) ('a' + c);
            boolean ng = greater || c > (target.charAt(pos) - 'a');
            if (dfs(pos + 1, ng)) return true;
            cnt[c]++;
        }
        return false;
    }
}
