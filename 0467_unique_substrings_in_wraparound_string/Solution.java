// LeetCode 0467 - Unique Substrings in Wraparound String
// https://leetcode.com/problems/unique-substrings-in-wraparound-string/

class Solution {
    public int findSubstringInWraproundString(String s) {
        int[] counts = new int[26];
        int length = 0;
        for (int index = 0; index < s.length(); index++) {
            if (index > 0 && (s.charAt(index) - s.charAt(index - 1) + 26) % 26 == 1) {
                length++;
            } else {
                length = 1;
            }
            int position = s.charAt(index) - 'a';
            counts[position] = Math.max(counts[position], length);
        }
        int total = 0;
        for (int count : counts) {
            total += count;
        }
        return total;
    }
}
