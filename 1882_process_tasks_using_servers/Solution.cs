// LeetCode 1882 - Process Tasks Using Servers
// https://leetcode.com/problems/process-tasks-using-servers/

public class Solution {
    public int[] AssignTasks(int[] servers, int[] tasks) {
        var available = new PriorityQueue<(int weight, int index), (int weight, int index)>();
        for (int index = 0; index < servers.Length; index++) {
            available.Enqueue((servers[index], index), (servers[index], index));
        }
        var busy = new PriorityQueue<(long finish, int weight, int index), (long finish, int weight, int index)>();
        var answer = new int[tasks.Length];
        long time = 0;

        for (int moment = 0; moment < tasks.Length; moment++) {
            int task = tasks[moment];
            time = Math.Max(time, moment);
            while (busy.Count > 0 && busy.Peek().finish <= time) {
                var (_, weight, index) = busy.Dequeue();
                available.Enqueue((weight, index), (weight, index));
            }
            while (available.Count == 0) {
                time = busy.Peek().finish;
                while (busy.Count > 0 && busy.Peek().finish <= time) {
                    var (_, weight, index) = busy.Dequeue();
                    available.Enqueue((weight, index), (weight, index));
                }
            }
            var (w, idx) = available.Dequeue();
            busy.Enqueue((time + task, w, idx), (time + task, w, idx));
            answer[moment] = idx;
        }
        return answer;
    }
}
