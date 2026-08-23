// LeetCode 3211 - Generate Binary Strings Without Adjacent Zeros
// https://leetcode.com/problems/generate-binary-strings-without-adjacent-zeros/

import java.util.ArrayList;
import java.util.List;

class Solution {
    private int n;
    private StringBuilder t;
    private List<String> ans;

    public List<String> validStrings(int n) {
        this.n = n;
        ans = new ArrayList<>();
        t = new StringBuilder();
        dfs(0);
        return ans;
    }

    private void dfs(int i) {
        if (i >= n) {
            ans.add(t.toString());
            return;
        }
        for (int j = 0; j < 2; j++) {
            if ((j == 0 && (i == 0 || t.charAt(i - 1) == '1')) || j == 1) {
                t.append((char) ('0' + j));
                dfs(i + 1);
                t.deleteCharAt(t.length() - 1);
            }
        }
    }
}
