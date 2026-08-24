// LeetCode 2449 - Minimum Number of Operations to Make Arrays Similar
// https://leetcode.com/problems/minimum-number-of-operations-to-make-arrays-similar/

import java.util.ArrayList

class Solution {
    fun makeSimilar(nums: IntArray, target: IntArray): Long {
            nums.sort()
            target.sort()
            var oddN = ArrayList()
            var evenN = ArrayList()
            var oddT = ArrayList()
            var evenT = ArrayList()
            for (x in nums) {
                if (x % 2 == 0) evenN.add(x)
                else oddN.add(x)
            }
            for (x in target) {
                if (x % 2 == 0) evenT.add(x)
                else oddT.add(x)
            }
            var ans: Long = 0
            var i: Int = 0
    while (i < oddN.size) {
    
                var diff: Int = oddN.get(i) - oddT.get(i)
                if (diff > 0) ans += diff / 2
    
    i = i + 1
    }
            var i: Int = 0
    while (i < evenN.size) {
    
                var diff: Int = evenN.get(i) - evenT.get(i)
                if (diff > 0) ans += diff / 2
    
    i = i + 1
    }
            return ans
    }
}
