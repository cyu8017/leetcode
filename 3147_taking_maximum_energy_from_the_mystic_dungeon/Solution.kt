// LeetCode 3147 - Taking Maximum Energy From the Mystic Dungeon
// https://leetcode.com/problems/taking-maximum-energy-from-the-mystic-dungeon/

class Solution {
    fun maximumEnergy(energy: IntArray, k: Int): Int {
        var ans = -(1  shl  30)
        var n = energy.size
        for (i in n - k until n) {
            var j = i, s = 0
            while (j >= 0) {
                s += energy[j]
                ans = maxOf(ans, s)
                j -= k
            }
        }
        return ans
    }
}
