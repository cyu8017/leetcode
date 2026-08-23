// LeetCode 3490 - Count Beautiful Numbers
// https://leetcode.com/problems/count-beautiful-numbers/

using System.Text;

public class Solution {
    string Itoa3490(int x) {
        if (x == 0) return "0";
        var b = new StringBuilder();
        while (x > 0) {
            b.Insert(0, (char)('0' + x % 10));
            x /= 10;
        }
        return b.ToString();
    }

    int CountBeautiful(int n) {
        if (n <= 0) return 0;
        string s = Itoa3490(n);
        int Dfs(int pos, bool tight, int sum, int prod, bool started) {
            if (pos == s.Length) {
                if (!started) return 0;
                return (sum > 0 && prod % sum == 0) ? 1 : 0;
            }
            int up = tight ? (s[pos] - '0') : 9;
            int ans = 0;
            for (int d = 0; d <= up; d++) {
                bool nt = tight && d == up;
                if (!started && d == 0) ans += Dfs(pos + 1, nt, 0, 1, false);
                else {
                    int ns = sum + d;
                    int np = !started ? d : prod * d;
                    ans += Dfs(pos + 1, nt, ns, np, true);
                }
            }
            return ans;
        }
        return Dfs(0, true, 0, 1, false);
    }

    public int BeautifulNumbers(int l, int r) {
        return CountBeautiful(r) - CountBeautiful(l - 1);
    }
}
