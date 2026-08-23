// LeetCode 0554 - Brick Wall
// https://leetcode.com/problems/brick-wall/

import java.util.HashMap;
import java.util.List;
import java.util.Map;

class Solution {
    public int leastBricks(List<List<Integer>> wall) {
        Map<Integer, Integer> edges = new HashMap<>();
        int best = 0;
        for (List<Integer> row : wall) {
            int width = 0;
            for (int i = 0; i + 1 < row.size(); ++i) {
                width += row.get(i);
                int count = edges.getOrDefault(width, 0) + 1;
                edges.put(width, count);
                best = Math.max(best, count);
            }
        }
        return wall.size() - best;
    }
}
