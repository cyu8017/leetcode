// LeetCode 3447 - Assign Elements to Groups with Constraints
// https://leetcode.com/problems/assign-elements-to-groups-with-constraints/

class Solution {
    fun assignElements(groups: IntArray, elements: IntArray): IntArray {
        val maxV = 100001
        var first = IntArray(maxV)
        first.fill(-1)
        for (i in 0 until elements.size) {
            var e = elements[i]
            if (e < maxV && first[e] == -1) first[e] = i
        }
        var ans = IntArray(groups.size)
        for (gi in 0 until groups.size) {
            var g = groups[gi]
            var best = -1
            var d = 1
            while (d * d <= g) {
                if (g % d == 0) {
                    if (first[d] != -1 && (best == -1 || first[d] < best)) best = first[d]
                    var other = g / d
                    if (first[other] != -1 && (best == -1 || first[other] < best)) best = first[other]
                }
                d = d + 1
            }
            ans[gi] = best
        }
        return ans
    }
}
