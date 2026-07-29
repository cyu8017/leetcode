// LeetCode 1073 - Adding Two Negabinary Numbers
// https://leetcode.com/problems/adding-two-negabinary-numbers/

class Solution {
    fun addNegabinary(arr1: IntArray, arr2: IntArray): IntArray {
        var i = arr1.lastIndex
        var j = arr2.lastIndex
        var carry = 0
        val ans = mutableListOf<Int>()
        while (i >= 0 || j >= 0 || carry != 0) {
            var total = carry
            if (i >= 0) total += arr1[i--]
            if (j >= 0) total += arr2[j--]
            ans.add(total and 1)
            carry = -(total shr 1)
        }
        while (ans.size > 1 && ans.last() == 0) ans.removeAt(ans.lastIndex)
        ans.reverse()
        return ans.toIntArray()
    }
}
