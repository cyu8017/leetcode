// LeetCode 0228 - Summary Ranges
// https://leetcode.com/problems/summary-ranges/

import java.util.ArrayList;
import java.util.List;

class Solution {
    public String[] summaryRanges(int[] nums) {
        List<String> result = new ArrayList<>();
        int index = 0;

        while (index < nums.length) {
            int start = nums[index];
            while (index + 1 < nums.length && nums[index + 1] == nums[index] + 1) {
                index++;
            }
            if (start == nums[index]) {
                result.add(String.valueOf(start));
            } else {
                result.add(start + "->" + nums[index]);
            }
            index++;
        }

        return result.toArray(new String[0]);
    }
}
