// LeetCode 0624 - Maximum Distance in Arrays
// https://leetcode.com/problems/maximum-distance-in-arrays/

import java.util.List;

class Solution {
    public int maxDistance(List<List<Integer>> arrays) {
        int minVal = arrays.get(0).get(0);
        int maxVal = arrays.get(0).get(arrays.get(0).size() - 1);
        int best = 0;
        for (int i = 1; i < arrays.size(); ++i) {
            List<Integer> arr = arrays.get(i);
            int first = arr.get(0);
            int last = arr.get(arr.size() - 1);
            best = Math.max(best, Math.max(Math.abs(last - minVal), Math.abs(maxVal - first)));
            minVal = Math.min(minVal, first);
            maxVal = Math.max(maxVal, last);
        }
        return best;
    }
}
