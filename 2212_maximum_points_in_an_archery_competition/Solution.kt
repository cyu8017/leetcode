// LeetCode 2212 - Maximum Points in an Archery Competition
// https://leetcode.com/problems/maximum-points-in-an-archery-competition/

class Solution {

    var bestScore: Int = -1

    var best: IntArray = IntArray(12)


    private fun dfs(i: Int, remain: Int, score: Int, bob: IntArray, aliceArrows: IntArray) {

            if (i == 12) {
                if (score > bestScore) {
                    bestScore = score
                    best = bob.copyOf()
                    if (remain > 0) best[0] += remain
                }
                return
            }
            dfs(i + 1, remain, score, bob, aliceArrows)
            var need = aliceArrows[i] + 1
            if (remain >= need) {
                bob[i] = need
                dfs(i + 1, remain - need, score + i, bob, aliceArrows)
                bob[i] = 0
            }

    }


    fun maximumBobPoints(numArrows: Int, aliceArrows: IntArray): IntArray {

            bestScore = -1
            best = IntArray(12)
            dfs(0, numArrows, 0, IntArray(12), aliceArrows)
            return best

    }

}
