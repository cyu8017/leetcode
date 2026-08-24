// LeetCode 2498 - Frog Jump II
// https://leetcode.com/problems/frog-jump-ii/

class Solution {
    fun maxJump(stones: IntArray): Int {
            var ans: Int = stones[1] - stones[0]
            var i: Int = 2
    while (i < stones.size) {
    
                var diff: Int = stones[i] - stones[i - 2]
                if (diff > ans) ans = diff
    
    i = i + 1
    }
            return ans
    }
}
