// LeetCode 2255 - Count Prefixes of a Given String
// https://leetcode.com/problems/count-prefixes-of-a-given-string/

class Solution {
    public int countPrefixes(String[] words, String s) {
        int ans = 0;
        for (var w : words)
            if (w.length() <= s.length() && s.startsWith(w)) ans++;
        return ans;
    }
}
