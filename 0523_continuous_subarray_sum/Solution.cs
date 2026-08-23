// LeetCode 0523 - Continuous Subarray Sum
// https://leetcode.com/problems/continuous-subarray-sum/

public class Solution {
    public bool CheckSubarraySum(int[] nums, int k) {
        Dictionary<int, int> remainders = new() { [0] = -1 };
        int prefix = 0;
        for (int index = 0; index < nums.Length; index++) {
            prefix += nums[index];
            int mod = k != 0 ? prefix % k : prefix;
            if (remainders.TryGetValue(mod, out int previous)) {
                if (index - previous >= 2) {
                    return true;
                }
            } else {
                remainders[mod] = index;
            }
        }
        return false;
    }
}
