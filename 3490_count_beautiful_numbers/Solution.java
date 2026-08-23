// LeetCode 3490 - Count Beautiful Numbers
// https://leetcode.com/problems/count-beautiful-numbers/

class Solution {
    private String s;

    private int countBeautiful(int n) {
        if (n <= 0) return 0;
        s = Integer.toString(n);
        return dfs(0, true, 0, 1, false);
    }

    private int dfs(int pos, boolean tight, int sum, int prod, boolean started) {
        if (pos == s.length()) {
            if (!started) return 0;
            return (sum > 0 && prod % sum == 0) ? 1 : 0;
        }
        int up = tight ? (s.charAt(pos) - '0') : 9;
        int ans = 0;
        for (int d = 0; d <= up; d++) {
            boolean nt = tight && d == up;
            if (!started && d == 0) ans += dfs(pos + 1, nt, 0, 1, false);
            else {
                int ns = sum + d;
                int np = !started ? d : prod * d;
                ans += dfs(pos + 1, nt, ns, np, true);
            }
        }
        return ans;
    }

    public int beautifulNumbers(int l, int r) {
        return countBeautiful(r) - countBeautiful(l - 1);
    }
}
