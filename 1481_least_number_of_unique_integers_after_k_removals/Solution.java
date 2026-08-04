// LeetCode 1481 - Least Number Of Unique Integers After K Removals
// https://leetcode.com/problems/least-number-of-unique-integers-after-k-removals/

import java.util.*;

class Solution {
    public int findLeastNumOfUniqueInts(int[] arr, int k) {
        Map<Integer, Integer> freq = new HashMap<>();
        for (int x : arr) freq.merge(x, 1, Integer::sum);
        List<Integer> counts = new ArrayList<>(freq.values());
        Collections.sort(counts);
        int removed = 0;
        for (int count : counts) {
            if (k < count) break;
            k -= count;
            removed++;
        }
        return counts.size() - removed;
    }
}
