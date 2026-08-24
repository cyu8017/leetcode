// LeetCode 2432 - The Employee That Worked on the Longest Task
// https://leetcode.com/problems/the-employee-that-worked-on-the-longest-task/

class Solution {
    fun hardestWorker(n: Int, logs: Array<IntArray>): Int {
            var ans: Int = logs[0][0]
            var best: Int = logs[0][1]
            var prev: Int = 0
            for (log in logs) {
                var dur: Int = log[1] - prev
                if (dur > best || (dur == best && log[0] < ans)) {
                    best = dur
                    ans = log[0]
                }
                prev = log[1]
            }
            return ans
    }
}
