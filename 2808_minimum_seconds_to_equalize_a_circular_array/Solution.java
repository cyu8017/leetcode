// LeetCode 2808 - Minimum Seconds to Equalize a Circular Array
// https://leetcode.com/problems/minimum-seconds-to-equalize-a-circular-array/

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

class Solution {
    public int minimumSeconds(List<Integer> nums) {
        int n = nums.size();
        var pos = new HashMap<Integer, List<Integer>>();
        for (int i = 0; i < n; i++) {
            if (!pos.containsKey(nums.get(i))) pos.put(nums.get(i), new ArrayList<Integer>());
            pos.get(nums.get(i)).add(i);
        }
        int ans = n;
        for (var p : pos.values()) {
            int maxGap = 0;
            for (int i = 0; i < p.size(); i++) {
                int gap = (i + 1 < p.size()) ? p[i + 1] - p[i] : p[0] + n - p[i];
                maxGap = Math.max(maxGap, gap / 2);
            }
            ans = Math.min(ans, maxGap);
        }
        return ans;
    }
}
