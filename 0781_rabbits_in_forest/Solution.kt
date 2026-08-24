// LeetCode 0781 - Rabbits in Forest
// https://leetcode.com/problems/rabbits-in-forest/

class Solution {
    fun numRabbits(answers: IntArray): Int {
        var counts = HashMap<Int, Int>()
        for (answer in answers) { counts.merge(answer, 1, Integer::sum) }
        var total = 0
        for (Map.Entry<Integer, Integer> e : counts.entrySet()) {
            var group = e.getKey() + 1
            var groups = (e.getValue() + group - 1) / group
            total += groups * group
        }
        return total
    }
}
