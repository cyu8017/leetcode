// LeetCode 1880 - Check if Word Equals Summation of Two Words
// https://leetcode.com/problems/check-if-word-equals-summation-of-two-words/

public class Solution {
    public bool IsSumEqual(string firstWord, string secondWord, string targetWord) {
        return Value(firstWord) + Value(secondWord) == Value(targetWord);
    }

    private static int Value(string word) {
        int result = 0;
        foreach (char ch in word) {
            result = result * 10 + (ch - 'a');
        }
        return result;
    }
}
