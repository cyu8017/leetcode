// LeetCode 0522 - Longest Uncommon Subsequence II
// https://leetcode.com/problems/longest-uncommon-subsequence-ii/

class Solution {
    public int findLUSlength(String[] strs) {
        int result = -1;
        for (int i = 0; i < strs.length; i++) {
            boolean uncommon = true;
            for (int j = 0; j < strs.length; j++) {
                if (i != j && isSubsequence(strs[i], strs[j])) {
                    uncommon = false;
                    break;
                }
            }
            if (uncommon) {
                result = Math.max(result, strs[i].length());
            }
        }
        return result;
    }

    private boolean isSubsequence(String target, String source) {
        int index = 0;
        for (int pos = 0; pos < source.length(); pos++) {
            if (index < target.length() && target.charAt(index) == source.charAt(pos)) {
                index++;
            }
        }
        return index == target.length();
    }
}
