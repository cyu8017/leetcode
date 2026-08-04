// LeetCode 1403 - Minimum Subsequence In Non Increasing Order
// https://leetcode.com/problems/minimum-subsequence-in-non-increasing-order/

import java.util.*;

class Solution {
    public List<Integer> minSubsequence(int[] nums) {
        Integer[] boxed = Arrays.stream(nums).boxed().toArray(Integer[]::new);
        Arrays.sort(boxed, Collections.reverseOrder());
        int total = 0;
        for (int x : nums) total += x;
        List<Integer> answer = new ArrayList<>();
        int chosen = 0;
        for (int value : boxed) {
            answer.add(value);
            chosen += value;
            if (chosen > total - chosen) return answer;
        }
        return answer;
    }
}
