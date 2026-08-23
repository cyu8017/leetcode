// LeetCode 3490 - Count Beautiful Numbers
// https://leetcode.com/problems/count-beautiful-numbers/

#include <string>
#include <functional>

class Solution {
    std::string itoa3490(int x) {
        if (x == 0) return "0";
        std::string b;
        while (x > 0) {
            b.insert(b.begin(), char('0' + x % 10));
            x /= 10;
        }
        return b;
    }
    int countBeautiful(int n) {
        if (n <= 0) return 0;
        std::string s = itoa3490(n);
        std::function<int(int, bool, int, int, bool)> dfs = [&](int pos, bool tight, int sum, int prod, bool started) -> int {
            if (pos == (int)s.size()) {
                if (!started) return 0;
                return (sum > 0 && prod % sum == 0) ? 1 : 0;
            }
            int up = tight ? (s[pos] - '0') : 9;
            int ans = 0;
            for (int d = 0; d <= up; d++) {
                bool nt = tight && d == up;
                if (!started && d == 0) ans += dfs(pos + 1, nt, 0, 1, false);
                else {
                    int ns = sum + d;
                    int np = !started ? d : prod * d;
                    ans += dfs(pos + 1, nt, ns, np, true);
                }
            }
            return ans;
        };
        return dfs(0, true, 0, 1, false);
    }
public:
    int beautifulNumbers(int l, int r) {
        return countBeautiful(r) - countBeautiful(l - 1);
    }
};
