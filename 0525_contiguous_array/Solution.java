// LeetCode 0525 - Contiguous Array
// https://leetcode.com/problems/contiguous-array/

import java.util.HashMap;
import java.util.Map;

class Solution {
    public int findMaxLength(int[] nums) {
        Map<Integer, Integer> counts = new HashMap<>();
        counts.put(0, -1);
        int balance = 0;
        int best = 0;
        for (int index = 0; index < nums.length; index++) {
            balance += nums[index] == 1 ? 1 : -1;
            if (counts.containsKey(balance)) {
                best = Math.max(best, index - counts.get(balance));
            } else {
                counts.put(balance, index);
            }
        }
        return best;
    }
}
