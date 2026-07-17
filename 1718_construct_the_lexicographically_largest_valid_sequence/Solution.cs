// LeetCode 1718 - Construct the Lexicographically Largest Valid Sequence
// https://leetcode.com/problems/construct-the-lexicographically-largest-valid-sequence/

public class Solution {
    public int[] ConstructDistancedSequence(int n) {
        int[] ans = new int[2 * n - 1];
        bool[] used = new bool[n + 1];
        Backtrack(0, n, ans, used);
        return ans;
    }

    private bool Backtrack(int i, int n, int[] ans, bool[] used) {
        while (i < ans.Length && ans[i] != 0) {
            i++;
        }
        if (i == ans.Length) {
            return true;
        }
        for (int value = n; value >= 1; value--) {
            if (used[value]) {
                continue;
            }
            if (value == 1) {
                ans[i] = 1;
                used[1] = true;
                if (Backtrack(i + 1, n, ans, used)) {
                    return true;
                }
                used[1] = false;
                ans[i] = 0;
            } else {
                int j = i + value;
                if (j < ans.Length && ans[j] == 0) {
                    ans[i] = value;
                    ans[j] = value;
                    used[value] = true;
                    if (Backtrack(i + 1, n, ans, used)) {
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
