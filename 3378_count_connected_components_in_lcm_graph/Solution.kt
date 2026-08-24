// LeetCode 3378 - Count Connected Components in LCM Graph
// https://leetcode.com/problems/count-connected-components-in-lcm-graph/

class Solution {
    private var parent: IntArray? = null

    private fun gcd(a: Int, b: Int): Int {
        while (b != 0) {
            var t = a % b
            a = b
            b = t
        }
        return a
    }

    private fun find(x: Int): Int {
        if (parent[x] != x) parent[x] = find(parent[x])
        return parent[x]
    }

    private fun unite(a: Int, b: Int) {
        var ra = find(a)
        var rb = find(b)
        if (ra != rb) parent[ra] = rb
    }

    fun countComponents(nums: IntArray, threshold: Int): Int {
        var n = nums.size
        parent = IntArray(n)
        for (i in 0 until n) { parent[i] = i }
        var idx = HashMap<Int, Int>()
        for (i in 0 until n) { idx[nums[i]] = i }
        for (d in 1 ..threshold) {
            var first = -1
            var m = d
            while (m <= threshold) {
                var i = idx[m]
                if (i != null) {
                    if (first == -1) first = i
                    else if ((long) nums[first] * nums[i] / gcd(nums[first], nums[i]) <= threshold)
                        unite(first, i)
                }
                m += d
            }
        }
        for (i in 0 until n) {
            for (j in i + 1 until n) {
                var a = nums[i]
                var b = nums[j]
                var g = gcd(a, b)
                if (a / g * b <= threshold) unite(i, j)
            }
        }
        var comp = HashSet<Int>()
        for (i in 0 until n) { comp.add(find(i)) }
        return comp.size
    }
}
