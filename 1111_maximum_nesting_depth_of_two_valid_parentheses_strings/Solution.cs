// LeetCode 1111 - Maximum Nesting Depth of Two Valid Parentheses Strings
// https://leetcode.com/problems/maximum-nesting-depth-of-two-valid-parentheses-strings/

public class Solution {
    public int[] MaxDepthAfterSplit(string seq) {
        int depth = 0;
        int[] ans = new int[seq.Length];
        for (int i = 0; i < seq.Length; i++) {
            if (seq[i] == '(') {
                ans[i] = depth % 2;
                depth++;
            } else {
                depth--;
                ans[i] = depth % 2;
            }
        }
        return ans;
    }
}
