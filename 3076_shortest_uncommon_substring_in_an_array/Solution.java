// LeetCode 3076 - Shortest Uncommon Substring in an Array
// https://leetcode.com/problems/shortest-uncommon-substring-in-an-array/

class Solution {
    public String[] shortestSubstrings(String[] arr) {
        int n = arr.length;
        String[] ans = new String[n];
        for (int i = 0; i < n; i++) ans[i] = "";
        for (int i = 0; i < n; i++) {
            String s = arr[i];
            int m = s.length();
            for (int j = 1; j <= m && ans[i].isEmpty(); j++) {
                for (int l = 0; l <= m - j; l++) {
                    String sub = s.substring(l, l + j);
                    if (ans[i].isEmpty() || ans[i].compareTo(sub) > 0) {
                        boolean ok = true;
                        for (int k = 0; k < n; k++) {
                            if (k != i && arr[k].contains(sub)) {
                                ok = false;
                                break;
                            }
                        }
                        if (ok) ans[i] = sub;
                    }
                }
            }
        }
        return ans;
    }
}
