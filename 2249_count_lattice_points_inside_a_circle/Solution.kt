// LeetCode 2249 - Count Lattice Points Inside a Circle
// https://leetcode.com/problems/count-lattice-points-inside-a-circle/

class Solution {

    fun countLatticePoints(circles: Array<IntArray>): Int {

            var seen = HashSet<Int>()
            for (c in circles) {
                var x = c[0]; var y = c[1]; var r = c[2]
                for (i in x - r..x + r) { for (var j = y - r } j <= y + r; j++)
                        if ((i - x) * (i - x) + (j - y) * (j - y) <= r * r)
                            seen.add((i << 32) | (j & 0xffffffffL))
            }
            return seen.size

    }

}
