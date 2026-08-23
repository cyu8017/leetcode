// LeetCode 3302 - Find the Lexicographically Smallest Valid Sequence
// https://leetcode.com/problems/find-the-lexicographically-smallest-valid-sequence/

public class Solution {
    bool CanFinish(string w1, string w2, int i, int j, bool usedSkip, int[] right) {
        int m = w2.Length;
        if (j >= m) return true;
        if (!usedSkip) {
            if (right[j] >= i) return true;
            if (j + 1 <= m && right[j + 1] > i) return true;
            if (right[j] > i) return true;
            return false;
        }
        return right[j] >= i;
    }

    public int[] ValidSequence(string word1, string word2) {
        int n = word1.Length, m = word2.Length;
        int[] right = new int[m + 1];
        right[m] = n;
        int j = m - 1;
        for (int i = n - 1; i >= 0 && j >= 0; i--) {
            if (word1[i] == word2[j]) {
                right[j] = i;
                j--;
            }
        }
        for (; j >= 0; j--) right[j] = -1;
        int[] ans = new int[m];
        bool usedSkip = false;
        int ii = 0;
        for (j = 0; j < m; j++) {
            bool found = false;
            while (ii < n) {
                if (word1[ii] == word2[j]) {
                    if (CanFinish(word1, word2, ii + 1, j + 1, usedSkip, right)) {
                        ans[j] = ii; ii++; found = true; break;
                    }
                } else if (!usedSkip) {
                    if (CanFinish(word1, word2, ii + 1, j + 1, true, right)) {
                        ans[j] = ii; ii++; usedSkip = true; found = true; break;
                    }
                }
                ii++;
            }
            if (!found) return new int[0];
        }
        return ans;
    }
}
