// LeetCode 0245 - Shortest Word Distance III
// https://leetcode.com/problems/shortest-word-distance-iii/

public class Solution {
    public int ShortestWordDistance(string[] wordsDict, string word1, string word2) {
        if (word1 == word2) {
            int previous = -1;
            int best = int.MaxValue;
            for (int index = 0; index < wordsDict.Length; index++) {
                if (wordsDict[index] == word1) {
                    if (previous >= 0) {
                        best = Math.Min(best, index - previous);
                    }
                    previous = index;
                }
            }
            return best;
        }

        int index1 = -1;
        int index2 = -1;
        int bestDistance = int.MaxValue;
        for (int index = 0; index < wordsDict.Length; index++) {
            string word = wordsDict[index];
            if (word == word1) {
                index1 = index;
                if (index2 >= 0) {
                    bestDistance = Math.Min(bestDistance, index - index2);
                }
            }
            if (word == word2) {
                index2 = index;
                if (index1 >= 0) {
                    bestDistance = Math.Min(bestDistance, index - index1);
                }
            }
        }
        return bestDistance;
    }
}
