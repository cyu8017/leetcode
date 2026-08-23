// LeetCode 0522 - Longest Uncommon Subsequence II
// https://leetcode.com/problems/longest-uncommon-subsequence-ii/

public class Solution {
    public int FindLUSlength(string[] strs) {
        int result = -1;
        for (int i = 0; i < strs.Length; i++) {
            bool uncommon = true;
            for (int j = 0; j < strs.Length; j++) {
                if (i != j && IsSubsequence(strs[i], strs[j])) {
                    uncommon = false;
                    break;
                }
            }
            if (uncommon) {
                result = Math.Max(result, strs[i].Length);
            }
        }
        return result;
    }

    private static bool IsSubsequence(string target, string source) {
        int index = 0;
        for (int pos = 0; pos < source.Length; pos++) {
            if (index < target.Length && target[index] == source[pos]) {
                index++;
            }
        }
        return index == target.Length;
    }
}
