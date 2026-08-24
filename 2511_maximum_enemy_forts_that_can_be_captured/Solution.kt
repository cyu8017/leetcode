// LeetCode 2511 - Maximum Enemy Forts That Can Be Captured
// https://leetcode.com/problems/maximum-enemy-forts-that-can-be-captured/

class Solution {
    fun captureForts(forts: IntArray): Int {
            var ans: Int = 0
            var prev: Int = -1
            var i: Int = 0
    while (i < forts.size) {
    
                if (forts[i] != 0) {
                    if (prev >= 0 && forts[prev] == -forts[i]) {
                        if (i - prev - 1 > ans) ans = i - prev - 1
                    }
                    prev = i
                }
    
    i = i + 1
    }
            return ans
    }
}
