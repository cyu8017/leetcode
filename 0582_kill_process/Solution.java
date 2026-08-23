// LeetCode 0582 - Kill Process
// https://leetcode.com/problems/kill-process/

import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Queue;

class Solution {
    public List<Integer> killProcess(List<Integer> pid, List<Integer> ppid, int kill) {
        Map<Integer, List<Integer>> children = new HashMap<>();
        for (int i = 0; i < pid.size(); ++i) {
            children.computeIfAbsent(ppid.get(i), k -> new ArrayList<>()).add(pid.get(i));
        }

        List<Integer> result = new ArrayList<>();
        Queue<Integer> queue = new ArrayDeque<>();
        queue.offer(kill);
        while (!queue.isEmpty()) {
            int process = queue.poll();
            result.add(process);
            List<Integer> kids = children.get(process);
            if (kids != null) {
                for (int child : kids) {
                    queue.offer(child);
                }
            }
        }
        return result;
    }
}
