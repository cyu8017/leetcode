// LeetCode 2768 - Number of Black Blocks
// https://leetcode.com/problems/number-of-black-blocks/

class Solution {
    fun countBlackBlocks(m: Int, n: Int, coordinates: Array<IntArray>): LongArray {
        var cnt = HashMap<Long, Int>()
        for (c in coordinates) {
            var x = c[0]
            var y = c[1]
            for (i in x - 1 ..x) {
                for (j in y - 1 ..y) {
                    if (i >= 0 && j >= 0 && i < m - 1 && j < n - 1) {
                        var key = (i  shl  32) | (j & 0xffffffffL)
                        cnt[key] = cnt.getOrDefault(key, 0 + 1)
                    }
                }
            }
        }
        var ans = LongArray(5)
        ans[0] = 1L * (m - 1) * (n - 1)
        for (v in cnt.values()) {
            ans[v]++
            ans[0]--
        }
        return ans
    }
}
