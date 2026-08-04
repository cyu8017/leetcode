// LeetCode 1402 - Reducing Dishes
// https://leetcode.com/problems/reducing-dishes/

class Solution {
    fun maxSatisfaction(satisfaction: IntArray): Int {
        satisfaction.sortDescending()
        var total = 0
        var answer = 0
        for (value in satisfaction) {
            if (total + value <= 0) break
            total += value
            answer += total
        }
        return answer
    }
}
