// LeetCode 2105 - Watering Plants II
// https://leetcode.com/problems/watering-plants-ii/

class Solution {
    fun minimumRefill(plants: IntArray, capacityA: Int, capacityB: Int): Int {
        var i: Int = 0, j = plants.size - 1
        var a: Int = capacityA, b = capacityB, ans = 0
        while (i < j) {
            if (a < plants[i]) { ans++; a = capacityA; }
            a -= plants[i++]
            if (b < plants[j]) { ans++; b = capacityB; }
            b -= plants[j--]
        }
        if (i == j) {
            if (a >= b) { if (a < plants[i]) ans++; }
            else if (b < plants[i]) ans++
        }
        return ans
    }
}
