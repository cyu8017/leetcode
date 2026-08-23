// LeetCode 0022 - Generate Parentheses
// https://leetcode.com/problems/generate-parentheses/

import java.util.ArrayList;
import java.util.List;

class Solution {
    public List<String> generateParenthesis(int n) {
        List<String> result = new ArrayList<>();
        backtrack(result, new StringBuilder(), n, 0, 0);
        return result;
    }

    private void backtrack(
        List<String> result,
        StringBuilder path,
        int n,
        int openCount,
        int closeCount
    ) {
        if (path.length() == 2 * n) {
            result.add(path.toString());
            return;
        }
        if (openCount < n) {
            path.append('(');
            backtrack(result, path, n, openCount + 1, closeCount);
            path.deleteCharAt(path.length() - 1);
        }
        if (closeCount < openCount) {
            path.append(')');
            backtrack(result, path, n, openCount, closeCount + 1);
            path.deleteCharAt(path.length() - 1);
        }
    }
}
