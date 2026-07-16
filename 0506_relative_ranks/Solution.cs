// LeetCode 0506 - Relative Ranks
// https://leetcode.com/problems/relative-ranks/

public class Solution {
    public string[] FindRelativeRanks(int[] score) {
        Dictionary<int, string> medals = new() {
            [1] = "Gold Medal",
            [2] = "Silver Medal",
            [3] = "Bronze Medal",
        };
        int[] order = score
            .Select((value, index) => (value, index))
            .OrderByDescending(item => item.value)
            .Select(item => item.index)
            .ToArray();
        string[] result = new string[score.Length];
        for (int rank = 0; rank < order.Length; rank++) {
            int index = order[rank];
            result[index] = medals.GetValueOrDefault(rank + 1, (rank + 1).ToString());
        }
        return result;
    }
}
