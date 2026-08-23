// LeetCode 3731 - Find Missing Elements
// https://leetcode.com/problems/find-missing-elements/

import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

class Solution {
    public int[] findMissingElements(int[] nums) {
        int mn = 100, mx = 0;
        var s = new HashSet<Integer>();
        for (int x : nums) {
            mn = Math.min(mn, x);
            mx = Math.max(mx, x);
            s.add(x);
        }
        var ans = new ArrayList<Integer>();
        for (int x = mn + 1; x < mx; x++) {
            if (!s.contains(x)) ans.add(x);
        }
        return ans.stream().mapToInt(Integer::intValue).toArray();
    }
}
