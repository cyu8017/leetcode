// LeetCode 0636 - Exclusive Time of Functions
// https://leetcode.com/problems/exclusive-time-of-functions/

using System.Collections.Generic;

public class Solution {
    public int[] ExclusiveTime(int n, IList<string> logs) {
        int[] result = new int[n];
        var stack = new List<int>();
        int prevTime = 0;
        foreach (string log in logs) {
            string[] parts = log.Split(':');
            int funcId = int.Parse(parts[0]);
            string eventType = parts[1];
            int time = int.Parse(parts[2]);
            if (eventType == "start") {
                if (stack.Count > 0) result[stack[^1]] += time - prevTime;
                stack.Add(funcId);
                prevTime = time;
            } else {
                result[stack[^1]] += time - prevTime + 1;
                stack.RemoveAt(stack.Count - 1);
                prevTime = time + 1;
            }
        }
        return result;
    }
}
