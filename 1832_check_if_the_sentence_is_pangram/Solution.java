// LeetCode 1832 - Check if the Sentence Is Pangram
// https://leetcode.com/problems/check-if-the-sentence-is-pangram/

class Solution {
    public boolean checkIfPangram(String sentence) {
        boolean[] seen = new boolean[26];
        for (int i = 0; i < sentence.length(); i++) {
            seen[sentence.charAt(i) - 'a'] = true;
        }
        for (boolean letter : seen) {
            if (!letter) {
                return false;
            }
        }
        return true;
    }
}
