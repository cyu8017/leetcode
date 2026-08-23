// LeetCode 0582 - Kill Process
// https://leetcode.com/problems/kill-process/

using System.Collections.Generic;

public class Solution {
    public IList<int> KillProcess(IList<int> pid, IList<int> ppid, int kill) {
        var children = new Dictionary<int, List<int>>();
        for (int i = 0; i < pid.Count; ++i) {
            if (!children.ContainsKey(ppid[i])) children[ppid[i]] = new List<int>();
            children[ppid[i]].Add(pid[i]);
        }
        var result = new List<int>();
        var queue = new Queue<int>();
        queue.Enqueue(kill);
        while (queue.Count > 0) {
            int process = queue.Dequeue();
            result.Add(process);
            if (children.TryGetValue(process, out var kids)) {
                foreach (int child in kids) queue.Enqueue(child);
            }
        }
        return result;
    }
}
