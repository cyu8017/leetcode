// LeetCode 2184 - Number of Ways to Build Sturdy Brick Wall
// https://leetcode.com/problems/number-of-ways-to-build-sturdy-brick-wall/

class Solution {
    private val masks = mutableListOf<Int>()
    private lateinit var bricks: IntArray

    private fun gen(remain: Int, mask: Int) {
        if (remain == 0) {
            masks.add(mask)
            return
        }
        for (b in bricks) {
            if (b <= remain) {
                var nm = mask
                if (remain - b > 0) nm = nm or (1 shl (remain - b))
                gen(remain - b, nm)
            }
        }
    }

    fun buildWall(height: Int, width: Int, bricks: IntArray): Int {
        val mod = 1_000_000_007
        this.bricks = bricks
        masks.clear()
        gen(width, 0)
        val m = masks.size
        val compat = Array(m) { mutableListOf<Int>() }
        for (i in 0 until m) {
            for (j in 0 until m) if ((masks[i] and masks[j]) == 0) compat[i].add(j)
        }
        var dp = IntArray(m) { 1 }
        for (h in 1 until height) {
            val ndp = IntArray(m)
            for (i in 0 until m) for (j in compat[i]) ndp[j] = (ndp[j] + dp[i]) % mod
            dp = ndp
        }
        var ans = 0
        for (v in dp) ans = (ans + v) % mod
        return ans
    }
}
