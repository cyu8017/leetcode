// LeetCode 0765 - Couples Holding Hands
// https://leetcode.com/problems/couples-holding-hands/

class Solution {
    fun minSwapsCouples(row: IntArray): Int {
        var pos = HashMap<Int, Int>()
        for (i in 0 until row.size) { pos[row[i]] = i }
        var swaps = 0
        var i = 0
        while (i < row.size) {
            var partner = row[i] ^ 1
            if (row[i + 1] == partner) continue
            var j = pos[partner]
            pos[row[i + 1]] = j
            row[j] = row[i + 1]
            row[i + 1] = partner
            pos[partner] = i + 1
            swaps++
            i += 2
        }
        return swaps
    }
}
