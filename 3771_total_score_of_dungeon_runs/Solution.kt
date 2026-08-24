// LeetCode 3771 - Total Score of Dungeon Runs
// https://leetcode.com/problems/total-score-of-dungeon-runs/

class Solution {
    fun totalScore(hp: Int, damage: IntArray, requirement: IntArray): Long {
        var n = damage.size
        var prefix = LongArray(n + 1)
        for (i in 0 until n) { prefix[i + 1] = prefix[i] + damage[i] }
        var answer = 1L * n * (n + 1) / 2
        for (j in 1 ..n) {
            var threshold = prefix[j] + (requirement[j - 1] - hp)
            var lo = 0
            var hi = j
            while (lo < hi) {
                var mid = (lo + hi) / 2
                if (prefix[mid] < threshold) lo = mid + 1
                else hi = mid
            }
            answer -= lo
        }
        return answer
    }
}
