// LeetCode 3441 - Minimum Cost Good Caption
// https://leetcode.com/problems/minimum-cost-good-caption/

public class Solution {
    public string MinCostGoodCaption(string caption) {
        int n = caption.Length;
        if (n < 3) return "";
        char[] ans = caption.ToCharArray();
        int i = 0;
        while (i < n) {
            int j = i;
            while (j < n && ans[j] == ans[i]) j++;
            if (j - i >= 3) { i = j; continue; }
            int need = 3 - (j - i);
            if (j + need <= n) {
                for (int t = 0; t < need; t++) ans[j + t] = ans[i];
                i = j + need;
            } else {
                char ch = 'a';
                if (i > 0) ch = ans[i - 1];
                else if (j < n) ch = caption[j];
                for (int t = i; t < n; t++) ans[t] = ch;
                break;
            }
        }
        i = 0;
        while (i < n) {
            int j = i;
            while (j < n && ans[j] == ans[i]) j++;
            if (j - i < 3) return "";
            i = j;
        }
        return new string(ans);
    }
}
