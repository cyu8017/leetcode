// LeetCode 2675 - Array of Objects to Matrix
// https://leetcode.com/problems/array-of-objects-to-matrix/

import java.util.*;

// JS array-of-objects-to-matrix stand-in
class Solution {
    public List<List<String>> jsonToMatrix(List<TreeMap<String, String>> arr) {
        TreeSet<String> keys = new TreeSet<>();
        for (TreeMap<String, String> obj : arr) keys.addAll(obj.keySet());
        List<List<String>> mat = new ArrayList<>();
        mat.add(new ArrayList<>(keys));
        for (TreeMap<String, String> obj : arr) {
            List<String> row = new ArrayList<>();
            for (String k : keys) row.add(obj.getOrDefault(k, ""));
            mat.add(row);
        }
        return mat;
    }
}
