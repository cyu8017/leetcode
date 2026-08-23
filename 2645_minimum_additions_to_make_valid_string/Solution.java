// LeetCode 2645 - Minimum Additions to Make Valid String
// https://leetcode.com/problems/minimum-additions-to-make-valid-string/

class Solution {
    public int addMinimum(String word) {
        int ans = 0, expect = 0, i = 0, n = word.length();
        while (i < n) {
            char need = (char) ('a' + expect);
            if (word.charAt(i) == need) i++;
            else ans++;
            expect = (expect + 1) % 3;
        }
        ans += (3 - expect) % 3;
        return ans;
    }
}
