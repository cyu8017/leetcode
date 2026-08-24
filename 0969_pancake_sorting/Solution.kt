// LeetCode 0969 - Pancake Sorting
// https://leetcode.com/problems/pancake-sorting/

class Solution {
    fun pancakeSort(arr: IntArray): List<Int> {
        val a = arr.copyOf()
        val ans = mutableListOf<Int>()
        for (size in a.size downTo 2) {
            val i = indexOf(a, size)
            if (i == size - 1) continue
            if (i > 0) {
                ans.add(i + 1)
                reverse(a, 0, i)
            }
            ans.add(size)
            reverse(a, 0, size - 1)
        }
        return ans
    }

    private fun indexOf(a: IntArray, v: Int): Int {
        for (i in a.indices) if (a[i] == v) return i
        return -1
    }

    private fun reverse(a: IntArray, l: Int, r: Int) {
        var l = l
        var r = r
        while (l < r) {
            val t = a[l]
            a[l] = a[r]
            a[r] = t
            l++
            r--
        }
    }
}
