// LeetCode 3041 - Maximize Consecutive Elements in an Array After Modification
// https://leetcode.com/problems/maximize-consecutive-elements-in-an-array-after-modification/

import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

class Solution {
    public int maxSelectedElements(int[] nums) {
        Arrays.sort(nums);
        var dp = new HashMap<Integer, Integer>();
        int ans = 0;
        for (int num : nums) {
            int dn = dp.getOrDefault(num, 0);
            int dnm1 = dp.getOrDefault(num - 1, 0);
            dp.put(num + 1, dn + 1);
            dp.put(num, dnm1 + 1);
            ans = Math.max(ans, Math.max(dp.get(num), dp.get(num + 1)));
        }
        return ans;
    }
}
