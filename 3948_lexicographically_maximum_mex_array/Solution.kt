// LeetCode 3948 - Lexicographically Maximum MEX Array
// https://leetcode.com/problems/lexicographically-maximum-mex-array/

class Solution {
    fun maxMexArray(nums: IntArray): IntArray {
        var n = nums.size
        var remaining = IntArray(n + 2)
        for (x in nums) {
            if (x <= n + 1) remaining[x]++
        }
        var mex = 0
        while (remaining[mex] > 0) mex++
        var answer = ArrayList<Int>()
        var seen = IntArray(n + 2)
        var stamp = 0
        var index = 0
        while (index < n) {
            if (mex == 0) {
                answer.add(0)
                var x = nums[index]
                if (x <= n + 1) remaining[x]--
                index++
                continue
            }
            stamp++
            var need = mex
            while (need > 0) {
                var x = nums[index]
                if (x < mex && seen[x] != stamp) {
                    seen[x] = stamp
                    need--
                }
                if (x <= n + 1) remaining[x]--
                index++
            }
            answer.add(mex)
            mex = 0
            while (remaining[mex] > 0) mex++
        }
        var out = IntArray(answer.size)
        for (i in 0 until out.size) { out[i] = answer[i] }
        return out
    }
}
