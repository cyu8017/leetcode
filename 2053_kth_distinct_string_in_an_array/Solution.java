// LeetCode 2053 - Kth Distinct String in an Array
// https://leetcode.com/problems/kth-distinct-string-in-an-array/

import java.util.*;

class Solution {
    public String kthDistinct(String[] arr, int k) {
        Map<String, Integer> freq = new HashMap<>();
        for (String s : arr) freq.merge(s, 1, Integer::sum);
        for (String s : arr) if (freq.get(s) == 1 && --k == 0) return s;
        return "";
    }
}
