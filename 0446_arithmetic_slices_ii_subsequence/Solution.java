// LeetCode 0446 - Arithmetic Slices II - Subsequence
// https://leetcode.com/problems/arithmetic-slices-ii-subsequence/

import java.util.HashMap;
import java.util.Map;

class Solution {
    public int numberOfArithmeticSlices(int[] nums) {
        int total = 0;
        Map<Long, Integer>[] differences = new Map[nums.length];
        for (int index = 0; index < nums.length; index++) {
            differences[index] = new HashMap<>();
        }

        for (int index = 0; index < nums.length; index++) {
            for (int previous = 0; previous < index; previous++) {
                long diff = (long) nums[index] - nums[previous];
                total += differences[previous].getOrDefault(diff, 0);
                differences[index].merge(diff, differences[previous].getOrDefault(diff, 0) + 1, Integer::sum);
            }
        }

        return total;
    }
}
