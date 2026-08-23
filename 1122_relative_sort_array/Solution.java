// LeetCode 1122 - Relative Sort Array
// https://leetcode.com/problems/relative-sort-array/

import java.util.*;

class Solution {
    public int[] relativeSortArray(int[] arr1, int[] arr2) {
        Map<Integer, Integer> count = new HashMap<>();
        for (int x : arr1) count.merge(x, 1, Integer::sum);
        List<Integer> ans = new ArrayList<>();
        for (int x : arr2) {
            int c = count.getOrDefault(x, 0);
            for (int i = 0; i < c; i++) ans.add(x);
            count.remove(x);
        }
        List<Integer> rest = new ArrayList<>(count.keySet());
        Collections.sort(rest);
        for (int x : rest) {
            int c = count.get(x);
            for (int i = 0; i < c; i++) ans.add(x);
        }
        int[] result = new int[ans.size()];
        for (int i = 0; i < ans.size(); i++) result[i] = ans.get(i);
        return result;
    }
}
