// LeetCode 1213 - Intersection of Three Sorted Arrays
// https://leetcode.com/problems/intersection-of-three-sorted-arrays/

import java.util.*;

class Solution {
    public List<Integer> arraysIntersection(int[] arr1, int[] arr2, int[] arr3) {
        Set<Integer> common = new HashSet<>();
        for (int x : arr1) common.add(x);
        Set<Integer> s2 = new HashSet<>();
        for (int x : arr2) s2.add(x);
        common.retainAll(s2);
        Set<Integer> s3 = new HashSet<>();
        for (int x : arr3) s3.add(x);
        common.retainAll(s3);
        List<Integer> ans = new ArrayList<>(common);
        Collections.sort(ans);
        return ans;
    }
}
