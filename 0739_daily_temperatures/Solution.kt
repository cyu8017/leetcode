// LeetCode 0739 - Daily Temperatures
// https://leetcode.com/problems/daily-temperatures/

class Solution {
    fun dailyTemperatures(temperatures: IntArray): IntArray {
        var answer = IntArray(temperatures.size)
        var stack = ArrayList<Int>()
        for (i in 0 until temperatures.size) {
            while (!stack.isEmpty() && temperatures[stack[stack.size - 1]] < temperatures[i]) {
                var prev = stack.removeAt(stack.size - 1)
                answer[prev] = i - prev
            }
            stack.add(i)
        }
        return answer
    }
}
