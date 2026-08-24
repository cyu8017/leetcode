// LeetCode 2244 - Minimum Rounds to Complete All Tasks
// https://leetcode.com/problems/minimum-rounds-to-complete-all-tasks/

class Solution {

    fun minimumRounds(tasks: IntArray): Int {

            var freq = HashMap<Int, Int>()
            for (t in tasks) {
                var c = freq.getOrDefault(t, 0)
                freq.put(t, c + 1)
            }
            var ans = 0
            for (c in freq.values) {
                if (c == 1) return -1
                ans += (c + 2) / 3
            }
            return ans

    }

}
