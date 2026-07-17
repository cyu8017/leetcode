// LeetCode 1880 - Check if Word Equals Summation of Two Words
// https://leetcode.com/problems/check-if-word-equals-summation-of-two-words/

class Solution {
    private int value(String word) {
        StringBuilder sb = new StringBuilder();
        for (char ch : word.toCharArray()) {
            sb.append(ch - 'a');
        }
        return Integer.parseInt(sb.toString());
    }

    public boolean isSumEqual(String firstWord, String secondWord, String targetWord) {
        return value(firstWord) + value(secondWord) == value(targetWord);
    }
}
