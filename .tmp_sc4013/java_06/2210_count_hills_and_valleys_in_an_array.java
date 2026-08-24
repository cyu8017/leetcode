// LeetCode 2210 - Count Hills and Valleys in an Array
// https://leetcode.com/problems/count-hills-and-valleys-in-an-array/

import java.util.Arrays;
import java.util.ArrayList;
import java.util.List;

class Solution {
    public int countHillValley(int[] nums) {
        var compact = new ArrayList<>(Arrays.asList(nums[0] ));
        for (int i = 1; i < nums.length; i++)
            if (nums[i] != compact.get(compact.size() - 1)) compact.add(nums[i]);
        int ans = 0;
        for (int i = 1; i + 1 < compact.size(); i++)
            if ((compact.get(i) > compact.get(i - 1) && compact.get(i) > compact.get(i + 1)) ||
                (compact.get(i) < compact.get(i - 1) && compact.get(i) < compact.get(i + 1)))
                ans++;
        return ans;
    }
}
