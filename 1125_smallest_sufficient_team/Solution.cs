// LeetCode 1125 - Smallest Sufficient Team
// https://leetcode.com/problems/smallest-sufficient-team/

using System.Collections.Generic;
using System.Numerics;

public class Solution {
    public int[] SmallestSufficientTeam(string[] req_skills, IList<IList<string>> people) {
        int m = req_skills.Length;
        int n = people.Count;
        int target = (1 << m) - 1;
        var skillId = new Dictionary<string, int>();
        for (int i = 0; i < m; i++) skillId[req_skills[i]] = i;
        int[] personMasks = new int[n];
        for (int i = 0; i < n; i++) {
            int mask = 0;
            foreach (string skill in people[i]) mask |= 1 << skillId[skill];
            personMasks[i] = mask;
        }
        long[] dp = new long[1 << m];
        for (int i = 0; i < dp.Length; i++) dp[i] = -1;
        dp[0] = 0;
        for (int state = 0; state <= target; state++) {
            if (dp[state] < 0) continue;
            for (int i = 0; i < n; i++) {
                int next = state | personMasks[i];
                if (next == state) continue;
                long cand = dp[state] | (1L << i);
                if (dp[next] < 0 || BitOperations.PopCount((ulong)cand) < BitOperations.PopCount((ulong)dp[next])) {
                    dp[next] = cand;
                }
            }
        }
        var ans = new List<int>();
        for (int i = 0; i < n; i++) if ((dp[target] & (1L << i)) != 0) ans.Add(i);
        return ans.ToArray();
    }
}
