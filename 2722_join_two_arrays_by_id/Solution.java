// LeetCode 2722 - Join Two Arrays by ID
// https://leetcode.com/problems/join-two-arrays-by-id/

import java.util.*;

// JS join-by-id stand-in for maps with int id
class Solution {
    public List<TreeMap<String, Integer>> join(
            List<TreeMap<String, Integer>> arr1,
            List<TreeMap<String, Integer>> arr2) {
        TreeMap<Integer, TreeMap<String, Integer>> byId = new TreeMap<>();
        merge(byId, arr1);
        merge(byId, arr2);
        return new ArrayList<>(byId.values());
    }

    private void merge(TreeMap<Integer, TreeMap<String, Integer>> byId, List<TreeMap<String, Integer>> arr) {
        for (TreeMap<String, Integer> obj : arr) {
            int id = obj.get("id");
            TreeMap<String, Integer> dest = byId.computeIfAbsent(id, z -> new TreeMap<>());
            dest.putAll(obj);
        }
    }
}
