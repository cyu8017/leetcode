// LeetCode 3074 - Apple Redistribution into Boxes
// https://leetcode.com/problems/apple-redistribution-into-boxes/

class Solution {
    fun minimumBoxes(apple: IntArray, capacity: IntArray): Int {
        capacity.sort()
        var s = 0
        for (x in apple) { s += x }
        var i = 1
        while (true) {
            s -= capacity[capacity.size - i]
            if (s <= 0) return i
            i++
        }
    }
}
