// LeetCode 3720 - Lexicographically Smallest Permutation Greater Than Target
// https://leetcode.com/problems/lexicographically-smallest-permutation-greater-than-target/

public class Solution {
    public string LexGreaterPermutation(string s, string target) {
        int[] cnt = new int[26];
        foreach (char c in s) cnt[c - 'a']++;
        int n = s.Length;
        char[] ans = new char[n];
        bool Dfs(int pos, bool greater) {
            if (pos == n) return greater;
            int start = greater ? 0 : (target[pos] - 'a');
            for (int c = start; c < 26; c++) {
                if (cnt[c] == 0) continue;
                cnt[c]--;
                ans[pos] = (char)('a' + c);
                bool ng = greater || c > (target[pos] - 'a');
                if (Dfs(pos + 1, ng)) return true;
                cnt[c]++;
            }
            return false;
        }
        if (Dfs(0, false)) return new string(ans);
        return "";
    }
}
