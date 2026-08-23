// LeetCode 2363 - Merge Similar Items
// https://leetcode.com/problems/merge-similar-items/

import java.util.ArrayList;
import java.util.List;
import java.util.Map;
import java.util.TreeMap;

class Solution {
    public List<List<Integer>> mergeSimilarItems(int[][] items1, int[][] items2) {
        TreeMap<Integer, Integer> mp = new TreeMap<>();
        for (int[] it : items1) mp.put(it[0], mp.getOrDefault(it[0], 0) + it[1]);
        for (int[] it : items2) mp.put(it[0], mp.getOrDefault(it[0], 0) + it[1]);
        List<List<Integer>> ans = new ArrayList<>();
        for (Map.Entry<Integer, Integer> e : mp.entrySet()) {
            ans.add(List.of(e.getKey(), e.getValue()));
        }
        return ans;
    }
}
