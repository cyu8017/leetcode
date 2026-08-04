// LeetCode 1436 - Destination City
// https://leetcode.com/problems/destination-city/

import java.util.*;

class Solution {
    public String destCity(List<List<String>> paths) {
        var starts = new HashSet<>();
        for (var p : paths) starts.add(p[0]);
        for (var p : paths) if (!starts.contains(p[1])) return p[1];
        return "";
    }
}
