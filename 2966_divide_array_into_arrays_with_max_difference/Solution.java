// LeetCode 2966 - Divide Array Into Arrays With Max Difference
// https://leetcode.com/problems/divide-array-into-arrays-with-max-difference/

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

class Solution {
    public int[][] divideArray(int[] nums, int k) {
        Arrays.sort(nums);
        List<int[]> ans = new ArrayList<>();
        for (int i = 0; i < nums.length; i += 3) {
            if (nums[i + 2] - nums[i] > k) return new int[0][];
            ans.add(new int[] { nums[i], nums[i + 1], nums[i + 2] });
        }
        return ans.toArray(new int[ans.size()][]);
    }
}
