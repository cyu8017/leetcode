// LeetCode 0683 - K Empty Slots
// https://leetcode.com/problems/k-empty-slots/

class Solution {
    fun kEmptySlots(bulbs: IntArray, k: Int): Int {
        var n = bulbs.size
        var days = IntArray(n)
        for (day in 1 ..n) { days[bulbs[day - 1] - 1] = day }
        var ans = Int.MAX_VALUE
        var i = 0
        while (i < n - k - 1) {
            var left = i
            var right = i + k + 1
            var j = left + 1
            while (j < right && days[j] > days[left] && days[j] > days[right]) j++
            if (j == right) {
                ans = minOf(ans, maxOf(days[left], days[right]))
                i++
            } else i = j
        }
        return ans == if (Int.MAX_VALUE) -1 else ans
    }
}
