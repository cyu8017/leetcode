// LeetCode 1560 - Most Visited Sector in a Circular Track
// https://leetcode.com/problems/most-visited-sector-in-a-circular-track/

using System.Collections.Generic;

public class Solution {
    public IList<int> MostVisited(int n, int[] rounds) {
        int start = rounds[0], end = rounds[rounds.Length - 1];
        var result = new List<int>();
        if (start <= end) {
            for (int i = start; i <= end; i++) result.Add(i);
        } else {
            for (int i = 1; i <= end; i++) result.Add(i);
            for (int i = start; i <= n; i++) result.Add(i);
        }
        return result;
    }
}
