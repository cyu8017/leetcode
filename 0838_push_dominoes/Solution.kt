// LeetCode 0838 - Push Dominoes
// https://leetcode.com/problems/push-dominoes/

class Solution {
    fun pushDominoes(dominoes: String): String {
        var arr = dominoes.toCharArray()
        var n = arr.size
        var force = IntArray(n)
        var f = 0
        for (i in 0 until n) {
            if (arr[i] == 'R') f = n
            else if (arr[i] == 'L') f = 0
            else f = maxOf(f - 1, 0)
            force[i] += f
        }
        f = 0
        for (i in n - 1 downTo 0) {
            if (arr[i] == 'L') f = n
            else if (arr[i] == 'R') f = 0
            else f = maxOf(f - 1, 0)
            force[i] -= f
        }
        for (i in 0 until n) {
            if (force[i] > 0) arr[i] = 'R'
            else if (force[i] < 0) arr[i] = 'L'
            else arr[i] = '.'
        }
        return String(arr)
    }
}
