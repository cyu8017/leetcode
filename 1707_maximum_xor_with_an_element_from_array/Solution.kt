// LeetCode 1707 - Maximum XOR With an Element From Array
// https://leetcode.com/problems/maximum-xor-with-an-element-from-array/

class Solution {
    fun maximizeXor(nums: IntArray, queries: Array<IntArray>): IntArray {
        nums.sort()
        val order = queries.indices.sortedBy { queries[it][1] }

        val children = ArrayList<IntArray>()
        children.add(intArrayOf(-1, -1))

        fun insert(num: Int) {
            var node = 0
            for (bit in 31 downTo 0) {
                val b = (num shr bit) and 1
                if (children[node][b] == -1) {
                    children[node][b] = children.size
                    children.add(intArrayOf(-1, -1))
                }
                node = children[node][b]
            }
        }

        val ans = IntArray(queries.size) { -1 }
        var added = 0
        for (qi in order) {
            val x = queries[qi][0]
            val limit = queries[qi][1]
            while (added < nums.size && nums[added] <= limit) {
                insert(nums[added])
                added++
            }
            if (added == 0) {
                continue
            }
            var node = 0
            var value = 0
            for (bit in 31 downTo 0) {
                val b = (x shr bit) and 1
                val want = b xor 1
                if (children[node][want] != -1) {
                    value = value or (1 shl bit)
                    node = children[node][want]
                } else {
                    node = children[node][b]
                }
            }
            ans[qi] = value
        }
        return ans
    }
}
