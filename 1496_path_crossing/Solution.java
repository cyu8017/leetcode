// LeetCode 1496 - Path Crossing
// https://leetcode.com/problems/path-crossing/

import java.util.*;

class Solution {
    public boolean isPathCrossing(String path) {
        int x = 0, y = 0;
        Set<String> seen = new HashSet<>();
        seen.add("0,0");
        for (char c : path.toCharArray()) {
            if (c == 'N') y++;
            else if (c == 'S') y--;
            else if (c == 'E') x++;
            else x--;
            String key = x + "," + y;
            if (!seen.add(key)) return true;
        }
        return false;
    }
}
