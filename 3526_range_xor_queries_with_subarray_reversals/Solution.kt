// LeetCode 3526 - Range XOR Queries with Subarray Reversals
// https://leetcode.com/problems/range-xor-queries-with-subarray-reversals/

class Solution {
    fun getResults(nums: IntArray, queries: Array<IntArray>): IntArray {
        val a = nums.clone()
        val ans = ArrayList<Int>()
        for (q in queries) {
            val typ = q[0]
            if (typ == 1) {
                var l = q[1]
                var r = q[2]
                while (l < r) {
                    val tmp = a[l]
                    a[l] = a[r]
                    a[r] = tmp
                    l++
                    r--
                }
            } else if (typ == 2) {
                val l = q[1]
                val r = q[2]
                var x = 0
                for (i in l..r) x = x xor a[i]
                ans.add(x)
            } else {
                a[q[1]] = q[2]
            }
        }
        return ans.toIntArray()
    }
}
