// LeetCode 1086 - High Five
// https://leetcode.com/problems/high-five/

using System.Collections.Generic;
using System.Linq;

public class Solution {
    public int[][] HighFive(int[][] items) {
        var scores = new Dictionary<int, List<int>>();
        foreach (var item in items) {
            int id = item[0], score = item[1];
            if (!scores.ContainsKey(id)) {
                scores[id] = new List<int>();
            }
            scores[id].Add(score);
        }
        var ans = new List<int[]>();
        foreach (int id in scores.Keys.OrderBy(x => x)) {
            var top = scores[id].OrderByDescending(x => x).Take(5).ToList();
            ans.Add(new[] { id, top.Sum() / 5 });
        }
        return ans.ToArray();
    }
}
