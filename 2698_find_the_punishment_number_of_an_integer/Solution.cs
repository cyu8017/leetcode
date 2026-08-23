// LeetCode 2698 - Find the Punishment Number of an Integer
// https://leetcode.com/problems/find-the-punishment-number-of-an-integer/

public class Solution {
    public int PunishmentNumber(int n) {
        bool Can(int sq, int target) {
            string s = sq.ToString();
            int m = s.Length;
            bool Dfs(int i, int sum) {
                if (i == m) return sum == target;
                int cur = 0;
                for (int j = i; j < m; j++) {
                    cur = cur * 10 + (s[j] - '0');
                    if (sum + cur > target) break;
                    if (Dfs(j + 1, sum + cur)) return true;
                }
                return false;
            }
            return Dfs(0, 0);
        }
        int ans = 0;
        for (int i = 1; i <= n; i++) {
            int sq = i * i;
            if (Can(sq, i)) ans += sq;
        }
        return ans;
    }
}
