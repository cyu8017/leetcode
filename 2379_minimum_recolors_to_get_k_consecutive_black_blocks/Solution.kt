// LeetCode 2379 - Minimum Recolors to Get K Consecutive Black Blocks
// https://leetcode.com/problems/minimum-recolors-to-get-k-consecutive-black-blocks/

class Solution {
    fun minimumRecolors(blocks: String, k: Int): Int {
        var white = 0
        for (i in 0 until k) if (blocks[i] == 'W') white++
        var ans = white
        for (i in k until blocks.length) {
            if (blocks[i] == 'W') white++
            if (blocks[i - k] == 'W') white--
            ans = minOf(ans, white)
        }
        return ans
    }
}
