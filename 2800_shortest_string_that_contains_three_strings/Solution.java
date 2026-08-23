// LeetCode 2800 - Shortest String That Contains Three Strings
// https://leetcode.com/problems/shortest-string-that-contains-three-strings/

class Solution {
    public String minimumString(String a, String b, String c) {
        String[][] perms = {
            {a, b, c}, {a, c, b}, {b, a, c}, {b, c, a}, {c, a, b}, {c, b, a}
        };
        String ans = "";
        for (String[] p : perms) {
            String cur = merge(merge(p[0], p[1]), p[2]);
            if (ans.isEmpty() || cur.length() < ans.length()
                    || (cur.length() == ans.length() && cur.compareTo(ans) < 0))
                ans = cur;
        }
        return ans;
    }

    private String merge(String x, String y) {
        if (x.contains(y)) return x;
        String best = x + y;
        int n = Math.min(x.length(), y.length());
        for (int i = n; i > 0; i--) {
            if (x.substring(x.length() - i).equals(y.substring(0, i))) {
                String cand = x + y.substring(i);
                if (cand.length() < best.length()
                        || (cand.length() == best.length() && cand.compareTo(best) < 0))
                    best = cand;
                break;
            }
        }
        return best;
    }
}
