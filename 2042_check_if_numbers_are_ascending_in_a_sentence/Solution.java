// LeetCode 2042 - Check if Numbers Are Ascending in a Sentence
// https://leetcode.com/problems/check-if-numbers-are-ascending-in-a-sentence/

class Solution {
    public boolean areNumbersAscending(String s) {
        int prev = -1;
        for (String tok : s.split(" ")) {
            if (tok.isEmpty()) continue;
            if (tok.charAt(0) >= '0' && tok.charAt(0) <= '9') {
                int v = Integer.parseInt(tok);
                if (v <= prev) return false;
                prev = v;
            }
        }
        return true;
    }
}
