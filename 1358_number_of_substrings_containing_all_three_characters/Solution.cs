// LeetCode 1358 - Number Of Substrings Containing All Three Characters
// https://leetcode.com/problems/number-of-substrings-containing-all-three-characters/

public class Solution {
    public int NumberOfSubstrings(string s) {
        int[] last = { -1, -1, -1 }; int ans = 0;
        for (int i = 0; i < s.Length; i++) {
            last[s[i] - 'a'] = i;
            ans += System.Math.Min(last[0], System.Math.Min(last[1], last[2])) + 1;
        }
        return ans;
    }
}
