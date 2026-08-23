// LeetCode 1718 - Construct the Lexicographically Largest Valid Sequence
// https://leetcode.com/problems/construct-the-lexicographically-largest-valid-sequence/

class Solution {
    public int[] constructDistancedSequence(int n) {
        int[] ans = new int[2 * n - 1];
        boolean[] used = new boolean[n + 1];
        backtrack(0, n, ans, used);
        return ans;
    }

    private boolean backtrack(int i, int n, int[] ans, boolean[] used) {
        while (i < ans.length && ans[i] != 0) {
            i++;
        }
        if (i == ans.length) {
            return true;
        }
        for (int value = n; value >= 1; value--) {
            if (used[value]) {
                continue;
            }
            if (value == 1) {
                ans[i] = 1;
                used[1] = true;
                if (backtrack(i + 1, n, ans, used)) {
                    return true;
                }
                used[1] = false;
                ans[i] = 0;
            } else {
                int j = i + value;
                if (j < ans.length && ans[j] == 0) {
                    ans[i] = value;
                    ans[j] = value;
                    used[value] = true;
                    if (backtrack(i + 1, n, ans, used)) {
                        return true;
                    }
                    used[value] = false;
                    ans[i] = 0;
                    ans[j] = 0;
                }
            }
        }
        return false;
    }
}
