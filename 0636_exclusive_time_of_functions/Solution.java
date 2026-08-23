// LeetCode 0636 - Exclusive Time of Functions
// https://leetcode.com/problems/exclusive-time-of-functions/

import java.util.ArrayDeque;
import java.util.Deque;
import java.util.List;

class Solution {
    public int[] exclusiveTime(int n, List<String> logs) {
        int[] result = new int[n];
        Deque<Integer> stack = new ArrayDeque<>();
        int prevTime = 0;
        for (String log : logs) {
            String[] parts = log.split(":");
            int funcId = Integer.parseInt(parts[0]);
            String event = parts[1];
            int time = Integer.parseInt(parts[2]);
            if (event.equals("start")) {
                if (!stack.isEmpty()) {
                    result[stack.peek()] += time - prevTime;
                }
                stack.push(funcId);
                prevTime = time;
            } else {
                result[stack.pop()] += time - prevTime + 1;
                prevTime = time + 1;
            }
        }
        return result;
    }
}
