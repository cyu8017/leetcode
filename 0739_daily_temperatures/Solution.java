// LeetCode 0739 - Daily Temperatures
// https://leetcode.com/problems/daily-temperatures/

import java.util.*;

class Solution {
    public int[] dailyTemperatures(int[] temperatures) {
        int[] answer = new int[temperatures.length];
        List<Integer> stack = new ArrayList<>();
        for (int i = 0; i < temperatures.length; i++) {
            while (!stack.isEmpty() && temperatures[stack.get(stack.size() - 1)] < temperatures[i]) {
                int prev = stack.remove(stack.size() - 1);
                answer[prev] = i - prev;
            }
            stack.add(i);
        }
        return answer;
    }
}
