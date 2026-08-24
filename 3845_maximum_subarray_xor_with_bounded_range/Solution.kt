// LeetCode 3845 - Maximum Subarray XOR with Bounded Range
// https://leetcode.com/problems/maximum-subarray-xor-with-bounded-range/

class Solution {
    private class Node {
        val next = IntArray(2)
        var count = 0
    }

    private var nodes: ArrayList<Node> = ArrayList()

    private fun add(x: Int, delta: Int) {
        var u = 0
        nodes[u].count += delta
        for (b in 15 downTo 0) {
            val bit = (x shr b) and 1
            if (nodes[u].next[bit] == 0) {
                nodes[u].next[bit] = nodes.size
                nodes.add(Node())
            }
            u = nodes[u].next[bit]
            nodes[u].count += delta
        }
    }

    private fun query(x: Int): Int {
        var u = 0
        var res = 0
        for (b in 15 downTo 0) {
            val bit = (x shr b) and 1
            val want = bit xor 1
            val v = nodes[u].next[want]
            if (v != 0 && nodes[v].count > 0) {
                res = res or (1 shl b)
                u = v
            } else {
                u = nodes[u].next[bit]
            }
        }
        return res
    }

    fun maxSubarrayXor(nums: IntArray, k: Int): Int {
        nodes = ArrayList()
        nodes.add(Node())
        val n = nums.size
        val pref = IntArray(n + 1)
        for (i in 0 until n) pref[i + 1] = pref[i] xor nums[i]
        val maxQ = ArrayList<Int>()
        val minQ = ArrayList<Int>()
        var left = 0
        var trieLeft = 0
        var ans = 0
        for (r in 0 until n) {
            val x = nums[r]
            while (maxQ.isNotEmpty() && nums[maxQ[maxQ.size - 1]] <= x) maxQ.removeAt(maxQ.size - 1)
            maxQ.add(r)
            while (minQ.isNotEmpty() && nums[minQ[minQ.size - 1]] >= x) minQ.removeAt(minQ.size - 1)
            minQ.add(r)
            while (nums[maxQ[0]] - nums[minQ[0]] > k) {
                if (maxQ[0] == left) maxQ.removeAt(0)
                if (minQ[0] == left) minQ.removeAt(0)
                left++
            }
            add(pref[r], 1)
            while (trieLeft < left) {
                add(pref[trieLeft], -1)
                trieLeft++
            }
            val cur = query(pref[r + 1])
            if (cur > ans) ans = cur
        }
        return ans
    }
}
