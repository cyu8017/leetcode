// LeetCode 1529 - Minimum Suffix Flips
// https://leetcode.com/problems/minimum-suffix-flips/

class Solution {
    fun minFlips(target: String): Int {
        var answer = 0
        var previous = '0'
        for (current in target) {
            if (current != previous) answer++
            previous = current
        }
        return answer
    }
}
