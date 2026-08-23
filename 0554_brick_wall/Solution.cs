// LeetCode 0554 - Brick Wall
// https://leetcode.com/problems/brick-wall/

using System.Collections.Generic;

public class Solution {
    public int LeastBricks(IList<IList<int>> wall) {
        var edges = new Dictionary<int, int>();
        int best = 0;
        foreach (var row in wall) {
            int width = 0;
            for (int i = 0; i + 1 < row.Count; ++i) {
                width += row[i];
                edges.TryGetValue(width, out int count);
                edges[width] = ++count;
                if (count > best) best = count;
            }
        }
        return wall.Count - best;
    }
}
