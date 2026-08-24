// LeetCode 2534 - Time Taken to Cross the Door
// https://leetcode.com/problems/time-taken-to-cross-the-door/

class Solution {
    fun timeTaken(arrival: IntArray, state: IntArray): IntArray {
        var n = arrival.size
        var ans = IntArray(n)
        var enter = ArrayDeque<Int>()
        var exitq = ArrayDeque<Int>()
        var i = 0
        var t = 0
        var prev = 1
        while (i < n || !enter.isEmpty() || !exitq.isEmpty()) {
            while (i < n && arrival[i] <= t) {
                if (state[i] == 0) enter.offer(i)
                else exitq.offer(i)
                i = i + 1
            }
            if (enter.isEmpty() && exitq.isEmpty()) {
                if (i < n) {
                    t = arrival[i]
                    prev = 1
                }
                continue
            }
            if (prev == 1) {
                if (!exitq.isEmpty()) {
                    ans[exitq.poll()] = t
                    prev = 1
                } else {
                    ans[enter.poll()] = t
                    prev = 0
                }
            } else {
                if (!enter.isEmpty()) {
                    ans[enter.poll()] = t
                    prev = 0
                } else {
                    ans[exitq.poll()] = t
                    prev = 1
                }
            }
            t = t + 1
        }
        return ans
    }
}
