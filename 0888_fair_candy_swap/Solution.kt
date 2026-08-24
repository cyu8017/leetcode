// LeetCode 0888 - Fair Candy Swap
// https://leetcode.com/problems/fair-candy-swap/

class Solution {
    fun fairCandySwap(aliceSizes: IntArray, bobSizes: IntArray): IntArray {
        var sumA = 0
        var sumB = 0
        for (a in aliceSizes) { sumA += a; }
        for (b in bobSizes) { sumB += b; }
        var diff = (sumA - sumB) / 2
        var bob = HashSet<Int>()
        for (b in bobSizes) { bob.add(b); }
        for (a in aliceSizes) {
            if (bob.contains(a - diff)) return intArrayOf(a, a - diff)
        }
        return IntArray(0)
    }
}
