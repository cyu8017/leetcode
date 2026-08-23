// LeetCode 2182 - Construct String With Repeat Limit
// https://leetcode.com/problems/construct-string-with-repeat-limit/

class Solution {
    public String repeatLimitedString(String s, int repeatLimit) {
        int[] freq = new int[26];
        for (int i = 0; i < s.length(); i++) freq[s.charAt(i) - 'a']++;
        StringBuilder ans = new StringBuilder();
        while (true) {
            boolean placed = false;
            for (int c = 25; c >= 0; c--) {
                if (freq[c] == 0) continue;
                if (ans.length() > 0 && ans.charAt(ans.length() - 1) - 'a' == c) {
                    boolean found = false;
                    for (int d = c - 1; d >= 0; d--) {
                        if (freq[d] > 0) {
                            ans.append((char) ('a' + d));
                            freq[d]--;
                            found = placed = true;
                            break;
                        }
                    }
                    if (!found) return ans.toString();
                    break;
                }
                int use = Math.min(freq[c], repeatLimit);
                for (int i = 0; i < use; i++) ans.append((char) ('a' + c));
                freq[c] -= use;
                placed = true;
                break;
            }
            if (!placed) break;
        }
        return ans.toString();
    }
}
