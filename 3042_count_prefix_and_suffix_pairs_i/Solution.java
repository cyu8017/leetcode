// LeetCode 3042 - Count Prefix and Suffix Pairs I
// https://leetcode.com/problems/count-prefix-and-suffix-pairs-i/

class Solution {
    public int countPrefixSuffixPairs(String[] words) {
        int ans = 0;
        for (int i = 0; i < words.length; i++) {
            String s = words[i];
            for (int j = i + 1; j < words.length; j++) {
                String t = words[j];
                if (t.length() >= s.length() && t.startsWith(s) && t.endsWith(s))
                    ans++;
            }
        }
        return ans;
    }
}
