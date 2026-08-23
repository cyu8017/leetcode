// LeetCode 0739 - Daily Temperatures
// https://leetcode.com/problems/daily-temperatures/

using System.Collections.Generic;

public class Solution {
    public int[] DailyTemperatures(int[] temperatures) {
        int[] answer = new int[temperatures.Length];
        var stack = new List<int>();
        for (int i = 0; i < temperatures.Length; i++) {
            while (stack.Count > 0 && temperatures[stack[stack.Count - 1]] < temperatures[i]) {
                int prev = stack[stack.Count - 1];
                stack.RemoveAt(stack.Count - 1);
                answer[prev] = i - prev;
            }
            stack.Add(i);
        }
        return answer;
    }
}
