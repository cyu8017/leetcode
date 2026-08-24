// LeetCode 1103 - Distribute Candies to People
// https://leetcode.com/problems/distribute-candies-to-people/

class Solution {
    fun distributeCandies(candies: Int, num_people: Int): IntArray {
        val ans = IntArray(num_people)
        var remaining = candies
        var give = 1
        var i = 0
        while (remaining > 0) {
            val take = minOf(give, remaining)
            ans[i] += take
            remaining -= take
            give++
            i = (i + 1) % num_people
        }
        return ans
    }
}
