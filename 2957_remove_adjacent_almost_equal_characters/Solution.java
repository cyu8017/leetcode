// LeetCode 2957 - Remove Adjacent Almost-Equal Characters
// https://leetcode.com/problems/remove-adjacent-almost-equal-characters/

class Solution {
    public int removeAlmostEqualCharacters(String word) {
        int ans = 0, n = word.length(), i = 1;
        while (i < n) {
            if (Math.abs(word.charAt(i) - word.charAt(i - 1)) <= 1) {
                ans++;
                i += 2;
            } else i++;
        }
        return ans;
    }
}
