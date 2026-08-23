// LeetCode 2100 - Find Good Days to Rob the Bank
// https://leetcode.com/problems/find-good-days-to-rob-the-bank/

public class Solution {
    public IList<int> GoodDaysToRobBank(int[] security, int time) {
        int n = security.Length;
        if (time == 0) {
            var all = new List<int>(n);
            for (int i = 0; i < n; i++) all.Add(i);
            return all;
        }
        int[] left = new int[n], right = new int[n];
        for (int i = 1; i < n; i++) if (security[i] <= security[i - 1]) left[i] = left[i - 1] + 1;
        for (int i = n - 2; i >= 0; i--) if (security[i] <= security[i + 1]) right[i] = right[i + 1] + 1;
        var ans = new List<int>();
        for (int i = time; i < n - time; i++)
            if (left[i] >= time && right[i] >= time) ans.Add(i);
        return ans;
    }
}
