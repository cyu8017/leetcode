// LeetCode 3682 - Minimum Index Sum of Common Elements
// https://leetcode.com/problems/minimum-index-sum-of-common-elements/

import java.util.HashMap;
import java.util.Map;

class Solution {
    public int minimumSum(int[] nums1, int[] nums2) {
        int inf = 1 << 30;
        Map<Integer, Integer> d = new HashMap<>();
        for (int i = 0; i < nums2.length; i++) d.putIfAbsent(nums2[i], i);
        int ans = inf;
        for (int i = 0; i < nums1.length; i++) {
            Integer j = d.get(nums1[i]);
            if (j != null) ans = Math.min(ans, i + j);
        }
        return ans == inf ? -1 : ans;
    }
}
