// LeetCode 3991 - Sort Array Using Prefix Reversals
// https://leetcode.com/problems/sort-array-using-prefix-reversals/

class Solution {
    fun sortArray(nums: IntArray, pre: IntArray): Int {
        val n = nums.size
        val start = nums.joinToString(",")
        val target = (0 until n).joinToString(",")
        if (start == target) return 0

        val lengths = pre.filter { it in 2..n }.toSortedSet().toList()
        val visited = hashSetOf(start)
        var queue = ArrayDeque<IntArray>()
        queue.add(nums.copyOf())
        var steps = 0

        while (queue.isNotEmpty()) {
            steps++
            val nextQueue = ArrayDeque<IntArray>()
            while (queue.isNotEmpty()) {
                val cur = queue.removeFirst()
                for (i in lengths) {
                    val nxt = cur.copyOf()
                    var l = 0
                    var r = i - 1
                    while (l < r) {
                        val tmp = nxt[l]
                        nxt[l] = nxt[r]
                        nxt[r] = tmp
                        l++
                        r--
                    }
                    val key = nxt.joinToString(",")
                    if (key == target) return steps
                    if (visited.add(key)) nextQueue.add(nxt)
                }
            }
            queue = nextQueue
        }
        return -1
    }
}
