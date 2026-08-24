// LeetCode 2293 - Min Max Game
// https://leetcode.com/problems/min-max-game/

class Solution {

    fun minMaxGame(nums: IntArray): Int {
        var _nums = nums

            while (_nums.size > 1) {
                var next = IntArray(_nums.size / 2)
                for (i in 0 until next.size) {
                    if (i % 2 == 0) next[i] = minOf(_nums[2 * i], _nums[2 * i + 1])
                    else next[i] = maxOf(_nums[2 * i], _nums[2 * i + 1])
                }
                _nums = next
            }
            return _nums[0]
    }

}
