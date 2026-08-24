// LeetCode 2453 - Destroy Sequential Targets
// https://leetcode.com/problems/destroy-sequential-targets/

import java.util.HashMap

class Solution {
    fun destroyTargets(nums: IntArray, space: Int): Int {
            var cnt: MutableMap<Int, Int> = HashMap()
            for (x in nums) {
                var m: Int = x % space
                cnt.put(m, cnt.getOrDefault(m, 0) + 1)
            }
            var bestCnt: Int = 0
            for (c in cnt.values()) if (c > bestCnt) bestCnt = c
            var ans: Int = 1000000000
            for (kv in cnt.entrySet()) {
                if (kv.getValue() == bestCnt) {
                    for (x in nums) {
                        if (x % space == kv.getKey() && x < ans) ans = x
                    }
                }
            }
            return ans
    }
}
