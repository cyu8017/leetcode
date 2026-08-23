// LeetCode 3678 - Smallest Absent Positive Greater Than Average
// https://leetcode.com/problems/smallest-absent-positive-greater-than-average/

import java.util.HashSet;
import java.util.Set;

class Solution {
    public int smallestAbsent(int[] nums) {
        var s = new HashSet<Integer>();
        int sum = 0;
        for (int x : nums) {
            s.add(x);
            sum += x;
        }
        int ans = Math.max(1, sum / nums.length + 1);
        while (s.contains(ans)) ans++;
        return ans;
    }
}
