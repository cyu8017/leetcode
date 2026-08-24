// LeetCode 0914 - X of a Kind in a Deck of Cards
// https://leetcode.com/problems/x-of-a-kind-in-a-deck-of-cards/

class Solution {
    fun hasGroupsSizeX(deck: IntArray): Boolean {
        val count = HashMap<Int, Int>()
        for (x in deck) count[x] = count.getOrDefault(x, 0) + 1
        var g = 0
        for (c in count.values) g = gcd(g, c)
        return g >= 2
    }

    private fun gcd(a: Int, b: Int): Int {
        var a = a
        var b = b
        while (b != 0) {
            val t = a % b
            a = b
            b = t
        }
        return a
    }
}
