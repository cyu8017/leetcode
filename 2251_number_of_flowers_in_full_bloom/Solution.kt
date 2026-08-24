// LeetCode 2251 - Number of Flowers in Full Bloom
// https://leetcode.com/problems/number-of-flowers-in-full-bloom/

class Solution {

    fun fullBloomFlowers(flowers: Array<IntArray>, people: IntArray): IntArray {

            var start = ArrayList<Int>()
            var end = ArrayList<Int>()
            for (f in flowers) {
                start.add(f[0])
                end.add(f[1])
            }
            start.sort()
            end.sort()
            var ans = IntArray(people.size)
            for (i in 0 until people.size) {
                var t = people[i]
                ans[i] = upperBound(start, t) - lowerBound(end, t)
            }
            return ans

    }


    private fun upperBound(a: MutableList<Int>, t: Int): Int {

            var lo = 0; var hi = a.size
            while (lo < hi) {
                var mid = (lo + hi) / 2
                if (a[mid] <= t) lo = mid + 1
                else hi = mid
            }
            return lo

    }


    private fun lowerBound(a: MutableList<Int>, t: Int): Int {

            var lo = 0; var hi = a.size
            while (lo < hi) {
                var mid = (lo + hi) / 2
                if (a[mid] < t) lo = mid + 1
                else hi = mid
            }
            return lo

    }

}
