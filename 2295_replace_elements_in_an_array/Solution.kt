// LeetCode 2295 - Replace Elements in an Array
// https://leetcode.com/problems/replace-elements-in-an-array/

class Solution {

    fun arrayChange(nums: IntArray, operations: Array<IntArray>): IntArray {

            var pos = HashMap<Int, Int>()
            for (i in 0 until nums.size) { pos.put(nums[i], i) }
            for (op in operations) {
                var i = pos[op[0]]
                nums[i] = op[1]
                pos.remove(op[0])
                pos.put(op[1], i)
            }
            return nums

    }

}
