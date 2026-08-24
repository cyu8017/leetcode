// LeetCode 0771 - Jewels and Stones
// https://leetcode.com/problems/jewels-and-stones/

class Solution {
    fun numJewelsInStones(jewels: String, stones: String): Int {
        var jewelSet = HashSet<Char>()
        for (ch in jewels.toCharArray()) { jewelSet.add(ch) }
        var count = 0
        for (stone in stones.toCharArray()) { if (jewelSet.contains(stone)) count++ }
        return count
    }
}
