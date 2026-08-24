// LeetCode 0875 - Koko Eating Bananas
// https://leetcode.com/problems/koko-eating-bananas/

class Solution {
    fun minEatingSpeed(piles: IntArray, h: Int): Int {
        var lo = 1
        var hi = 0
        for (p in piles) { hi = maxOf(hi, p) }
        while (lo < hi) {
            var mid = (lo + hi) / 2
            var hours = 0
            for (p in piles) { hours += (p + mid - 1) / mid }
            if (hours <= h) hi = mid
            else lo = mid + 1
        }
        return lo
    }
}
