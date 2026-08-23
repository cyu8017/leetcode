// LeetCode 3955 - Valid Binary Strings With Cost Limit
// https://leetcode.com/problems/valid-binary-strings-with-cost-limit/

import java.util.ArrayList;
import java.util.List;

class Solution {
    public List<String> generateValidStrings(int n, int k) {
        List<String> ans = new ArrayList<>();
        StringBuilder path = new StringBuilder();
        dfs(0, 0, n, k, path, ans);
        return ans;
    }

    private void dfs(int i, int tot, int n, int k, StringBuilder path, List<String> ans) {
        if (i >= n) {
            ans.add(path.toString());
            return;
        }
        path.append('0');
        dfs(i + 1, tot, n, k, path, ans);
        path.deleteCharAt(path.length() - 1);
        if ((path.length() == 0 || path.charAt(path.length() - 1) == '0') && tot + i <= k) {
            path.append('1');
            dfs(i + 1, tot + i, n, k, path, ans);
            path.deleteCharAt(path.length() - 1);
        }
    }
}
