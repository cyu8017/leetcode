// LeetCode 0243 - Shortest Word Distance
// https://leetcode.com/problems/shortest-word-distance/

public class Solution {
    public int ShortestWordDistance(string[] wordsDict, string word1, string word2) {
        int index1 = -1;
        int index2 = -1;
        int best = int.MaxValue;
        for (int index = 0; index < wordsDict.Length; index++) {
            string word = wordsDict[index];
            if (word == word1) {
                index1 = index;
                if (index2 >= 0) {
                    best = Math.Min(best, index - index2);
                }
            }
            if (word == word2) {
                index2 = index;
                if (index1 >= 0) {
                    best = Math.Min(best, index - index1);
                }
            }
        }
        return best;
    }
}
