// LeetCode 0949 - Largest Time for Given Digits
// https://leetcode.com/problems/largest-time-for-given-digits/

class Solution {
    fun largestTimeFromDigits(arr: IntArray): String {
        arr.sort()
        var best = ""
        do {
            var hours = 10 * arr[0] + arr[1]
            var minutes = 10 * arr[2] + arr[3]
            if (hours < 24 && minutes < 60) {
                var cand = String.format("%02d:%02d", hours, minutes)
                if (cand.compareTo(best) > 0) best = cand
            }
        } while (nextPermutation(arr))
        return best
    }

    private fun nextPermutation(a: IntArray): Boolean {
        var i = a.size - 2
        while (i >= 0 && a[i] >= a[i + 1]) i--
        if (i < 0) return false
        var j = a.size - 1
        while (a[j] <= a[i]) j--
        var tmp = a[i]; a[i] = a[j]; a[j] = tmp
        var l = i + 1
        var r = a.size - 1
        while (l < r) {
            tmp = a[l]; a[l] = a[r]; a[r] = tmp
            l++, r--
        }
        return true
    }
}
