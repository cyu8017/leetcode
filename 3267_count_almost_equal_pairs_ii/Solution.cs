// LeetCode 3267 - Count Almost Equal Pairs II
// https://leetcode.com/problems/count-almost-equal-pairs-ii/

public class Solution {
    string PadNum(int x) {
        if (x == 0) return "0";
        var b = new System.Text.StringBuilder();
        while (x > 0) {
            b.Insert(0, (char)('0' + x % 10));
            x /= 10;
        }
        return b.ToString();
    }

    bool CanWithSwaps(char[] sa, string sb, int maxSwap) {
        bool Dfs(int start, int left) {
            string cur = new string(sa);
            if (cur == sb) return true;
            if (left == 0) return false;
            for (int i = start; i < sa.Length; i++) {
                if (sa[i] == sb[i]) continue;
                for (int j = i + 1; j < sa.Length; j++) {
                    if (sa[j] == sb[i]) {
                        char tmp = sa[i]; sa[i] = sa[j]; sa[j] = tmp;
                        if (Dfs(i + 1, left - 1)) return true;
                        tmp = sa[i]; sa[i] = sa[j]; sa[j] = tmp;
                    }
                }
                return false;
            }
            return new string(sa) == sb;
        }
        return Dfs(0, maxSwap);
    }

    bool AlmostEqual(int a, int b) {
        string sa = PadNum(a), sb = PadNum(b);
        while (sa.Length < sb.Length) sa = "0" + sa;
        while (sb.Length < sa.Length) sb = "0" + sb;
        if (sa == sb) return true;
        return CanWithSwaps(sa.ToCharArray(), sb, 2);
    }

    public int CountPairs(int[] nums) {
        int ans = 0;
        for (int i = 0; i < nums.Length; i++)
            for (int j = i + 1; j < nums.Length; j++)
                if (AlmostEqual(nums[i], nums[j])) ans++;
        return ans;
    }
}
