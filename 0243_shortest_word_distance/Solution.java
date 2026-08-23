// LeetCode 0243 - Shortest Word Distance
// https://leetcode.com/problems/shortest-word-distance/

class Solution {
    public int shortestWordDistance(String[] wordsDict, String word1, String word2) {
        int index1 = -1;
        int index2 = -1;
        int best = Integer.MAX_VALUE;
        for (int index = 0; index < wordsDict.length; index++) {
            String word = wordsDict[index];
            if (word.equals(word1)) {
                index1 = index;
                if (index2 >= 0) {
                    best = Math.min(best, index - index2);
                }
            }
            if (word.equals(word2)) {
                index2 = index;
                if (index1 >= 0) {
                    best = Math.min(best, index - index1);
                }
            }
        }
        return best;
    }
}
