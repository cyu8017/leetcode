// LeetCode 2844 - Minimum Operations to Make a Special Number
// https://leetcode.com/problems/minimum-operations-to-make-a-special-number/

class Solution {
    public int minimumOperations(String num) {
        int n = num.length();
        int ans = n;
        boolean has0 = false;
        for (int i = 0; i < n; i++) if (num.charAt(i) == '0') has0 = true;
        if (has0) ans = Math.min(ans, n - 1);
        String[] targets = {"00", "25", "50", "75"};
        for (String t : targets) {
            int j = n - 1;
            while (j >= 0 && num.charAt(j) != t.charAt(1)) j--;
            if (j < 0) continue;
            int i = j - 1;
            while (i >= 0 && num.charAt(i) != t.charAt(0)) i--;
            if (i < 0) continue;
            ans = Math.min(ans, n - i - 2);
        }
        return ans;
    }
}
