// LeetCode 0818 - Race Car
// https://leetcode.com/problems/race-car/

class Solution {
    fun racecar(target: Int): Int {
        var queue = ArrayDeque<IntArray>()
        queue.offer(intArrayOf(0, 1, 0))
        var seen = HashSet<Long>()
        seen.add(key(0, 1))
        while (!queue.isEmpty()) {
            var cur = queue.poll()
            var pos = cur[0]
            var speed = cur[1]
            var steps = cur[2]
            if (pos == target) return steps
            var nxtPos = pos + speed
            var nxtSpeed = speed * 2
            if (!seen.contains(key(nxtPos, nxtSpeed)) && kotlin.math.abs(nxtPos) < target * 2) {
                seen.add(key(nxtPos, nxtSpeed))
                queue.offer(intArrayOf(nxtPos, nxtSpeed, steps + 1))
            }
            var revSpeed = if (speed > 0) -1 else 1
            if (seen.add(key(pos, revSpeed))) {
                queue.offer(intArrayOf(pos, revSpeed, steps + 1))
            }
        }
        return -1
    }

    private fun key(pos: Int, speed: Int): Long {
        return (pos  shl  20) ^ (speed & 0xfffffL)
    }
}
