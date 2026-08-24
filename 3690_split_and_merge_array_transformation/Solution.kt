// LeetCode 3690 - Split and Merge Array Transformation
// https://leetcode.com/problems/split-and-merge-array-transformation/

class Solution {
    private var n = 0

    private fun toArr(nums: List<Int>): IntArray {
        val t = IntArray(6)
        for (i in 0 until n) t[i] = nums[i]
        return t
    }

    private fun key(a: IntArray): String = a.joinToString(",")

    fun minSplitMerge(nums1: IntArray, nums2: IntArray): Int {
        n = nums1.size
        val startL = ArrayList<Int>()
        val targetL = ArrayList<Int>()
        for (i in 0 until n) {
            startL.add(nums1[i])
            targetL.add(nums2[i])
        }
        val start = toArr(startL)
        val target = toArr(targetL)
        val vis = HashSet<String>()
        vis.add(key(start))
        var q = ArrayList<IntArray>()
        q.add(start)
        var ans = 0
        while (true) {
            val nq = ArrayList<IntArray>()
            for (cur in q) {
                if (cur.contentEquals(target)) return ans
                for (l in 0 until n) {
                    for (r in l until n) {
                        val remain = ArrayList<Int>()
                        val sub = ArrayList<Int>()
                        for (i in 0 until l) remain.add(cur[i])
                        for (i in r + 1 until n) remain.add(cur[i])
                        for (i in l..r) sub.add(cur[i])
                        for (pos in 0..remain.size) {
                            val nxtSlice = ArrayList<Int>()
                            nxtSlice.addAll(remain.subList(0, pos))
                            nxtSlice.addAll(sub)
                            nxtSlice.addAll(remain.subList(pos, remain.size))
                            val nxt = toArr(nxtSlice)
                            val k = key(nxt)
                            if (k !in vis) {
                                vis.add(k)
                                nq.add(nxt)
                            }
                        }
                    }
                }
            }
            q = nq
            ans++
        }
    }
}
