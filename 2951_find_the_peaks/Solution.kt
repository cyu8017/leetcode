// LeetCode 2951 - Find the Peaks
// https://leetcode.com/problems/find-the-peaks/

class Solution {
    fun findPeaks(mountain: IntArray): MutableList<Int> {
        val ans = ArrayList<Int>()
        var i = 1
        while (i + 1 < mountain.size) {
            if (mountain[i] > mountain[i - 1] && mountain[i] > mountain[i + 1]) {
                ans.add(i)
            }
            i++
        }
        return ans
    }
}
