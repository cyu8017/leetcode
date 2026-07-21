// LeetCode 1813 - Sentence Similarity III
// https://leetcode.com/problems/sentence-similarity-iii/

public class Solution {
    public bool AreSentencesSimilar(string sentence1, string sentence2) {
        string[] words1 = sentence1.Split(' ');
        string[] words2 = sentence2.Split(' ');
        int n1 = words1.Length, n2 = words2.Length;

        int i = 0;
        while (i < n1 && i < n2 && words1[i] == words2[i]) i++;
        if (i == n1 || i == n2) return true;

        int j1 = n1 - 1, j2 = n2 - 1;
        while (j1 >= i && j2 >= i && words1[j1] == words2[j2]) {
            j1--;
            j2--;
        }
        return j1 < i || j2 < i;
    }
}
