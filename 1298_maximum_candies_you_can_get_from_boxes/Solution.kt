// LeetCode 1298 - Maximum Candies You Can Get from Boxes
// https://leetcode.com/problems/maximum-candies-you-can-get-from-boxes/

class Solution {
    fun maxCandies(
        status: IntArray,
        candies: IntArray,
        keys: Array<IntArray>,
        containedBoxes: Array<IntArray>,
        initialBoxes: IntArray
    ): Int {
        val owned = initialBoxes.toMutableSet()
        val opened = mutableSetOf<Int>()
        val queue = ArrayDeque<Int>()
        for (box in initialBoxes) if (status[box] == 1) queue.add(box)
        var total = 0
        while (queue.isNotEmpty()) {
            val box = queue.removeFirst()
            if (box in opened || status[box] == 0) continue
            opened.add(box)
            total += candies[box]
            for (key in keys[box]) {
                status[key] = 1
                if (key in owned && key !in opened) queue.add(key)
            }
            for (child in containedBoxes[box]) {
                owned.add(child)
                if (status[child] == 1 && child !in opened) queue.add(child)
            }
        }
        return total
    }
}
