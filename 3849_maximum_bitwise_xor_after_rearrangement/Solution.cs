// LeetCode 3849 - Maximum Bitwise Xor After Rearrangement
// https://leetcode.com/problems/maximum-bitwise-xor-after-rearrangement/

public class Solution {
    public string MaximumXor(string s, string t) {
        int[] cnt = new int[2];
        foreach (char c in t) cnt[c - '0']++;
        char[] ans = new char[s.Length];
        for (int i = 0; i < s.Length; i++) ans[i] = '0';
        for (int i = 0; i < s.Length; i++) {
            int x = s[i] - '0';
            if (cnt[x ^ 1] > 0) {
                cnt[x ^ 1]--;
                ans[i] = '1';
            } else {
                cnt[x]--;
                ans[i] = '0';
            }
        }
        return new string(ans);
    }
}
