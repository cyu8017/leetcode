// LeetCode 0975 - Odd Even Jump
// https://leetcode.com/problems/odd-even-jump/

class Solution {
    fun oddEvenJumps(arr: IntArray): Int {
        val n = arr.size
        val nextHigher = IntArray(n)
        val nextLower = IntArray(n)
        var order = Array(n) { it }
        order.sortWith { i, j -> if (arr[i] == arr[j]) i.compareTo(j) else arr[i].compareTo(arr[j]) }
        val stack = mutableListOf<Int>()
        for (i in order) {
            while (stack.isNotEmpty() && stack.last() < i) {
                nextHigher[stack.removeAt(stack.size - 1)] = i
            }
            stack.add(i)
        }
        stack.clear()
        order.sortWith { i, j -> if (arr[i] == arr[j]) i.compareTo(j) else arr[j].compareTo(arr[i]) }
        for (i in order) {
            while (stack.isNotEmpty() && stack.last() < i) {
                nextLower[stack.removeAt(stack.size - 1)] = i
            }
            stack.add(i)
        }
        val odd = BooleanArray(n)
        val even = BooleanArray(n)
        odd[n - 1] = true
        even[n - 1] = true
        for (i in n - 2 downTo 0) {
            if (nextHigher[i] != 0) odd[i] = even[nextHigher[i]]
            if (nextLower[i] != 0) even[i] = odd[nextLower[i]]
        }
        return odd.count { it }
    }
}
