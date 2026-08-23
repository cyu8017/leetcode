// LeetCode 3302 - Find the Lexicographically Smallest Valid Sequence
// https://leetcode.com/problems/find-the-lexicographically-smallest-valid-sequence/

class Solution {
    private boolean canFinish(String w1, String w2, int i, int j, boolean usedSkip, int[] right) {
        int m = w2.length();
        if (j >= m) return true;
        if (!usedSkip) {
            if (right[j] >= i) return true;
            if (j + 1 <= m && right[j + 1] > i) return true;
            if (right[j] > i) return true;
            return false;
        }
        return right[j] >= i;
    }

    public int[] validSequence(String word1, String word2) {
        int n = word1.length(), m = word2.length();
        int[] right = new int[m + 1];
        right[m] = n;
        int j = m - 1;
        for (int i = n - 1; i >= 0 && j >= 0; i--) {
            if (word1.charAt(i) == word2.charAt(j)) {
                right[j] = i;
                j--;
            }
        }
        for (; j >= 0; j--) right[j] = -1;
        int[] ans = new int[m];
        boolean usedSkip = false;
        int i = 0;
        for (j = 0; j < m; j++) {
            boolean found = false;
            while (i < n) {
                if (word1.charAt(i) == word2.charAt(j)) {
                    if (canFinish(word1, word2, i + 1, j + 1, usedSkip, right)) {
                        ans[j] = i;
                        i++;
                        found = true;
                        break;
                    }
                } else if (!usedSkip) {
                    if (canFinish(word1, word2, i + 1, j + 1, true, right)) {
                        ans[j] = i;
                        i++;
                        usedSkip = true;
                        found = true;
                        break;
                    }
                }
                i++;
            }
            if (!found) return new int[0];
        }
        return ans;
    }
}
