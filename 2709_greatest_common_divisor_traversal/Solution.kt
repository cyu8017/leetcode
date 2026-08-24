// LeetCode 2709 - Greatest Common Divisor Traversal
// https://leetcode.com/problems/greatest-common-divisor-traversal/

class Solution {
    private lateinit var parent: IntArray

    fun canTraverseAllPairs(nums: IntArray): Boolean {
        val n = nums.size
        if (n == 1) return true
        var mx = nums[0]
        for (x in nums) if (x > mx) mx = x
        parent = IntArray(mx + 1) { it }
        val has = BooleanArray(mx + 1)
        for (x in nums) {
            if (x == 1) return false
            has[x] = true
        }
        val sieve = IntArray(mx + 1)
        for (i in 2..mx) {
            if (sieve[i] == 0) {
                var j = i
                while (j <= mx) {
                    if (sieve[j] == 0) sieve[j] = i
                    if (has[j]) unite(i, j)
                    j += i
                }
            }
        }
        val root = find(nums[0])
        for (x in nums) if (find(x) != root) return false
        return true
    }

    private fun find(x: Int): Int {
        if (parent[x] != x) parent[x] = find(parent[x])
        return parent[x]
    }

    private fun unite(a: Int, b: Int) {
        val ra = find(a)
        val rb = find(b)
        if (ra != rb) parent[ra] = rb
    }
}
