// LeetCode 1257 - Smallest Common Region
// https://leetcode.com/problems/smallest-common-region/

import java.util.*;

class Solution {
    public String findSmallestRegion(List<List<String>> regions, String region1, String region2) {
        Map<String, String> parent = new HashMap<>();
        for (List<String> group : regions) {
            for (int i = 1; i < group.size(); i++) parent.put(group.get(i), group.get(0));
        }
        Set<String> ancestors = new HashSet<>();
        while (region1 != null) {
            ancestors.add(region1);
            region1 = parent.get(region1);
        }
        while (!ancestors.contains(region2)) region2 = parent.get(region2);
        return region2;
    }
}

