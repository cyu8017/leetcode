// LeetCode 1813 - Sentence Similarity III
// https://leetcode.com/problems/sentence-similarity-iii/

class Solution {
    public boolean areSentencesSimilar(String sentence1, String sentence2) {
        String[] words1 = sentence1.split(" ");
        String[] words2 = sentence2.split(" ");
        int n1 = words1.length;
        int n2 = words2.length;

        int i = 0;
        while (i < n1 && i < n2 && words1[i].equals(words2[i])) {
            i++;
        }
        if (i == n1 || i == n2) {
            return true;
        }

        int j1 = n1 - 1;
        int j2 = n2 - 1;
        while (j1 >= i && j2 >= i && words1[j1].equals(words2[j2])) {
            j1--;
            j2--;
        }
        return j1 < i || j2 < i;
    }
}
