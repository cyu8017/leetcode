// LeetCode 2606 - Find the Substring With Maximum Cost
// https://leetcode.com/problems/find-the-substring-with-maximum-cost/

class Solution {
    public int maximumCostSubstring(String s, String chars, int[] vals) {
        int[] val = new int[26];
        for (int i = 0; i < 26; ++i) val[i] = i + 1;
        for (int i = 0; i < chars.length(); ++i) val[chars.charAt(i) - 'a'] = vals[i];
        int best = 0, cur = 0;
        for (char c : s.toCharArray()) {
            cur += val[c - 'a'];
            if (cur < 0) cur = 0;
            if (cur > best) best = cur;
        }
        return best;
    }
}
