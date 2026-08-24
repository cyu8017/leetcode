// LeetCode 2515 - Shortest Distance to Target String in a Circular Array
// https://leetcode.com/problems/shortest-distance-to-target-string-in-a-circular-array/

class Solution {
    fun closestTarget(words: Array<String>, target: String, startIndex: Int): Int {
            var n: Int = words.size
            var best: Int = -1
            var i: Int = 0
    while (i < n) {
    
                if (words[i] == target) {
                    var d: Int = i - startIndex
                    if (d < 0) d = -d
                    if (n - d < d) d = n - d
                    if (best < 0 || d < best) best = d
                }
    
    i = i + 1
    }
            return best
    }
}
