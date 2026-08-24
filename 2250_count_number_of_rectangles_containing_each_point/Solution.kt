// LeetCode 2250 - Count Number of Rectangles Containing Each Point
// https://leetcode.com/problems/count-number-of-rectangles-containing-each-point/

class Solution {

    fun countRectangles(rectangles: Array<IntArray>, points: Array<IntArray>): IntArray {

            @SuppressWarnings("unchecked")
            var byH = arrayOfNulls<ArrayList>(101)
            for (h in 0..100) { byH[h] = ArrayList<Int>() }
            for (r in rectangles) byH[r[1]].add(r[0])
            for (h in 1..100) { Collections.sort(byH[h]) }
            var ans = IntArray(points.size)
            for (i in 0 until points.size) {
                var x = points[i][0]; var y = points[i][1]; var cnt = 0
                for (h in y..100) {
                    var xs = byH[h]
                    var lo = 0; var hi = xs.size
                    while (lo < hi) {
                        var mid = (lo + hi) / 2
                        if (xs[mid] < x) lo = mid + 1
                        else hi = mid
                    }
                    cnt += xs.size - lo
                }
                ans[i] = cnt
            }
            return ans

    }

}
