// LeetCode 1313 - Decompress Run Length Encoded List
// https://leetcode.com/problems/decompress-run-length-encoded-list/

import java.util.*;

class Solution {
    public int[] decompressRLElist(int[] nums) {
        List<Integer> answer = new ArrayList<>();
        for (int i = 0; i < nums.length; i += 2) {
            for (int j = 0; j < nums[i]; j++) answer.add(nums[i + 1]);
        }
        int[] out = new int[answer.size()];
        for (int i = 0; i < answer.size(); i++) out[i] = answer.get(i);
        return out;
    }
}
