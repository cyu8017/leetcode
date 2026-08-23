// LeetCode 0624 - Maximum Distance in Arrays
// https://leetcode.com/problems/maximum-distance-in-arrays/

using System.Collections.Generic;

public class Solution {
    public int MaxDistance(IList<IList<int>> arrays) {
        int minVal = arrays[0][0];
        int maxVal = arrays[0][arrays[0].Count - 1];
        int best = 0;
        for (int i = 1; i < arrays.Count; ++i) {
            int first = arrays[i][0];
            int last = arrays[i][arrays[i].Count - 1];
            best = System.Math.Max(best, System.Math.Max(System.Math.Abs(last - minVal), System.Math.Abs(maxVal - first)));
            if (first < minVal) minVal = first;
            if (last > maxVal) maxVal = last;
        }
        return best;
    }
}
