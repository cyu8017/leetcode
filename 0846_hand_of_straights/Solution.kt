// LeetCode 0846 - Hand of Straights
// https://leetcode.com/problems/hand-of-straights/

class Solution {
    fun isNStraightHand(hand: IntArray, groupSize: Int): Boolean {
        if (hand.size % groupSize != 0) return false
        var count = TreeMap<Int, Int>()
        for (x in hand) { count.merge(x, 1, Integer::sum) }
        while (!count.isEmpty()) {
            var start = count.firstKey()
            for (x in start until start + groupSize) {
                var c = count[x]
                if (c == null) return false
                if (c == 1) count.remove(x)
                else count[x] = c - 1
            }
        }
        return true
    }
}
