// LeetCode 3762 - Minimum Operations To Equalize Subarrays
// https://leetcode.com/problems/minimum_operations_to_equalize_subarrays/

class Solution {
    private class Node() {
        var left = 0
        var right = 0
        var count = 0
        var sum = 0L

        constructor(o: Node) : this() {
            left = o.left
            right = o.right
            count = o.count
            sum = o.sum
        }
    }

    private lateinit var nodes: ArrayList<Node>

    fun minOperations(nums: IntArray, k: Int, queries: Array<IntArray>): LongArray {
        val n = nums.size
        val quotient = IntArray(n)
        val remainder = IntArray(n)
        var values = IntArray(n)
        for (i in 0 until n) {
            quotient[i] = nums[i] / k
            remainder[i] = nums[i] % k
            values[i] = quotient[i]
        }
        values.sort()
        var vu = 1
        for (i in 1 until n) {
            if (values[i] != values[vu - 1]) values[vu++] = values[i]
        }
        values = values.copyOf(vu)

        nodes = ArrayList()
        nodes.add(Node())
        val roots = IntArray(n + 1)
        val umax = values.size - 1
        for (i in 0 until n) {
            val position = lowerBound(values, quotient[i])
            roots[i + 1] = update(roots[i], 0, umax, position, quotient[i])
        }

        val logv = IntArray(n + 1)
        for (i in 2..n) logv[i] = logv[i / 2] + 1
        val levels = logv[n] + 1
        val minTable = Array(levels) { IntArray(0) }
        val maxTable = Array(levels) { IntArray(0) }
        minTable[0] = remainder.copyOf()
        maxTable[0] = remainder.copyOf()
        for (level in 1 until levels) {
            val length = n - (1 shl level) + 1
            minTable[level] = IntArray(length)
            maxTable[level] = IntArray(length)
            val half = 1 shl (level - 1)
            for (i in 0 until length) {
                minTable[level][i] = minOf(minTable[level - 1][i], minTable[level - 1][i + half])
                maxTable[level][i] = maxOf(maxTable[level - 1][i], maxTable[level - 1][i + half])
            }
        }

        val answer = LongArray(queries.size)
        for (qi in queries.indices) {
            val left = queries[qi][0]
            val right = queries[qi][1]
            val length = right - left + 1
            val level = logv[length]
            val offset = right - (1 shl level) + 1
            val minR = minOf(minTable[level][left], minTable[level][offset])
            val maxR = maxOf(maxTable[level][left], maxTable[level][offset])
            if (minR != maxR) {
                answer[qi] = -1
                continue
            }
            val medianIndex = kth(roots[right + 1], roots[left], 0, umax, (length + 1) / 2)
            val median = values[medianIndex]
            val stats = prefixStats(roots[right + 1], roots[left], 0, umax, medianIndex)
            val leftCount = stats[0].toInt()
            val leftSum = stats[1]
            val totalSum = nodes[roots[right + 1]].sum - nodes[roots[left]].sum
            answer[qi] = 1L * median * leftCount - leftSum + (totalSum - leftSum) - 1L * median * (length - leftCount)
        }
        return answer
    }

    private fun update(previous: Int, lo: Int, hi: Int, position: Int, value: Int): Int {
        val current = nodes.size
        nodes.add(Node(nodes[previous]))
        nodes[current].count++
        nodes[current].sum += value
        if (lo < hi) {
            val mid = (lo + hi) / 2
            if (position <= mid) {
                nodes[current].left = update(nodes[previous].left, lo, mid, position, value)
            } else {
                nodes[current].right = update(nodes[previous].right, mid + 1, hi, position, value)
            }
        }
        return current
    }

    private fun kth(rightRoot: Int, leftRoot: Int, lo: Int, hi: Int, rank: Int): Int {
        if (lo == hi) return lo
        val leftCount = nodes[nodes[rightRoot].left].count - nodes[nodes[leftRoot].left].count
        val mid = (lo + hi) / 2
        if (rank <= leftCount) return kth(nodes[rightRoot].left, nodes[leftRoot].left, lo, mid, rank)
        return kth(nodes[rightRoot].right, nodes[leftRoot].right, mid + 1, hi, rank - leftCount)
    }

    private fun prefixStats(rightRoot: Int, leftRoot: Int, lo: Int, hi: Int, end: Int): LongArray {
        if (end < lo) return longArrayOf(0, 0)
        if (hi <= end) {
            return longArrayOf(
                (nodes[rightRoot].count - nodes[leftRoot].count).toLong(),
                nodes[rightRoot].sum - nodes[leftRoot].sum,
            )
        }
        val mid = (lo + hi) / 2
        val left = prefixStats(nodes[rightRoot].left, nodes[leftRoot].left, lo, mid, end)
        var count = left[0]
        var sum = left[1]
        if (end > mid) {
            val right = prefixStats(nodes[rightRoot].right, nodes[leftRoot].right, mid + 1, hi, end)
            count += right[0]
            sum += right[1]
        }
        return longArrayOf(count, sum)
    }

    private fun lowerBound(a: IntArray, x: Int): Int {
        var lo = 0
        var hi = a.size
        while (lo < hi) {
            val mid = (lo + hi) / 2
            if (a[mid] < x) lo = mid + 1 else hi = mid
        }
        return lo
    }
}
