// LeetCode 1338 - Reduce Array Size To The Half
// https://leetcode.com/problems/reduce-array-size-to-the-half/

import java.util.*;

class Solution {
    public int minSetSize(int[] arr) {
        Map<Integer, Integer> freq = new HashMap<>();
        for (int x : arr) freq.merge(x, 1, Integer::sum);
        List<Integer> counts = new ArrayList<>(freq.values());
        counts.sort(Collections.reverseOrder());
        int removed = 0;
        for (int i = 0; i < counts.size(); i++) {
            removed += counts.get(i);
            if (removed * 2 >= arr.length) return i + 1;
        }
        return 0;
    }
}
