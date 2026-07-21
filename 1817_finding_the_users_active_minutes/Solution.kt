// LeetCode 1817 - Finding the Users Active Minutes
// https://leetcode.com/problems/finding-the-users-active-minutes/

class Solution {
    fun findingUsersActiveMinutes(logs: Array<IntArray>, k: Int): IntArray {
        val userMinutes = HashMap<Int, HashSet<Int>>()
        for (log in logs) {
            userMinutes.getOrPut(log[0]) { HashSet() }.add(log[1])
        }
        val answer = IntArray(k)
        for (minutes in userMinutes.values) {
            val uam = minutes.size
            if (uam <= k) answer[uam - 1]++
        }
        return answer
    }
}
