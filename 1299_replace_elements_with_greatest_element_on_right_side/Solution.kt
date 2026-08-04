// LeetCode 1299 - Replace Elements with Greatest Element on Right Side
// https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side/

class Solution {
    fun replaceElements(arr: IntArray): IntArray {
        var greatest = -1
        for (i in arr.lastIndex downTo 0) {
            val current = arr[i]
            arr[i] = greatest
            greatest = maxOf(greatest, current)
        }
        return arr
    }
}
