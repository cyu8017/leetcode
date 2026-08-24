// LeetCode 2218 - Maximum Value of K Coins From Piles
// https://leetcode.com/problems/maximum-value-of-k-coins-from-piles/

class Solution {

    fun maxValueOfCoins(piles: MutableList<MutableList<Int>>, k: Int): Int {

            var dp = IntArray(k + 1)
            for (pile in piles) {
                var ndp = dp.copyOf()
                var sum = 0
                run {
    var take = 1
    while (take <= pile.size && take <= k) {

                    sum += pile[take - 1]
                    for (j in take..k) { ndp[j] = maxOf(ndp[j], dp[j - take] + sum) }

    take++
    }
    }
                dp = ndp
            }
            return dp[k]

    }

}
