// LeetCode 1684 - Count the Number of Consistent Strings
// https://leetcode.com/problems/count-the-number-of-consistent-strings/

class Solution {
    public int countConsistentStrings(String allowed, String[] words) {
        boolean[] ok = new boolean[26];
        for (int i = 0; i < allowed.length(); i++) {
            ok[allowed.charAt(i) - 'a'] = true;
        }
        int ans = 0;
        for (String word : words) {
            boolean good = true;
            for (int i = 0; i < word.length(); i++) {
                if (!ok[word.charAt(i) - 'a']) {
                    good = false;
                    break;
                }
            }
            if (good) {
                ans++;
            }
        }
        return ans;
    }
}
