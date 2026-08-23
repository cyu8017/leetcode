// LeetCode 1859 - Sorting the Sentence
// https://leetcode.com/problems/sorting-the-sentence/

class Solution {
    public String sortSentence(String s) {
        String[] tokens = s.split(" ");
        String[] ordered = new String[tokens.length];

        for (String token : tokens) {
            int position = token.charAt(token.length() - 1) - '1';
            ordered[position] = token.substring(0, token.length() - 1);
        }

        return String.join(" ", ordered);
    }
}
