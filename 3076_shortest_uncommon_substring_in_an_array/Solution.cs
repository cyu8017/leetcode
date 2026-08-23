// LeetCode 3076 - Shortest Uncommon Substring in an Array
// https://leetcode.com/problems/shortest-uncommon-substring-in-an-array/

public class Solution {
    public string[] ShortestSubstrings(string[] arr) {
        int n = arr.Length;
        string[] ans = new string[n];
        for (int i = 0; i < n; i++) ans[i] = "";
        for (int i = 0; i < n; i++) {
            string s = arr[i];
            int m = s.Length;
            for (int j = 1; j <= m && ans[i].Length == 0; j++) {
                for (int l = 0; l <= m - j; l++) {
                    string sub = s.Substring(l, j);
                    if (ans[i].Length == 0 || string.CompareOrdinal(ans[i], sub) > 0) {
                        bool ok = true;
                        for (int k = 0; k < n; k++) {
                            if (k != i && arr[k].Contains(sub)) {
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
