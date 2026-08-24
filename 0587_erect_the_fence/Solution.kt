// LeetCode 0587 - Erect the Fence
// https://leetcode.com/problems/erect-the-fence/

class Solution {
    fun outerTrees(trees: Array<IntArray>): Array<IntArray> {
        val points = trees.copyOf()
        points.sortWith(compareBy({ it[0] }, { it[1] }))
        if (points.size <= 1) return points

        val lower = build(points)
        val reversed = Array(points.size) { points[points.size - 1 - it] }
        val upper = build(reversed)

        val seen = HashSet<String>()
        val unique = ArrayList<IntArray>()
        for (i in 0 until lower.size - 1) addUnique(unique, seen, lower[i])
        for (i in 0 until upper.size - 1) addUnique(unique, seen, upper[i])
        return unique.toTypedArray()
    }

    private fun build(ordered: Array<IntArray>): List<IntArray> {
        val hull = ArrayList<IntArray>()
        for (point in ordered) {
            while (hull.size >= 2 && cross(hull[hull.size - 2], hull[hull.size - 1], point) < 0) {
                hull.removeAt(hull.size - 1)
            }
            hull.add(point)
        }
        return hull
    }

    private fun cross(o: IntArray, a: IntArray, b: IntArray): Long =
        (a[0] - o[0]).toLong() * (b[1] - o[1]) - (a[1] - o[1]).toLong() * (b[0] - o[0])

    private fun addUnique(unique: MutableList<IntArray>, seen: MutableSet<String>, point: IntArray) {
        val key = "${point[0]},${point[1]}"
        if (seen.add(key)) unique.add(point)
    }
}
