// LeetCode 1090 - Largest Values From Labels
// https://leetcode.com/problems/largest-values-from-labels/

import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

class Solution {
    public int largestValsFromLabels(int[] values, int[] labels, int numWanted, int useLimit) {
        int n = values.length;
        Integer[] idx = new Integer[n];
        for (int i = 0; i < n; i++) {
            idx[i] = i;
        }
        Arrays.sort(idx, (a, b) -> Integer.compare(values[b], values[a]));
        Map<Integer, Integer> used = new HashMap<>();
        int ans = 0, taken = 0;
        for (int i : idx) {
            if (taken == numWanted) {
                break;
            }
            int label = labels[i];
            int count = used.getOrDefault(label, 0);
            if (count < useLimit) {
                used.put(label, count + 1);
                ans += values[i];
                taken++;
            }
        }
        return ans;
    }
}
