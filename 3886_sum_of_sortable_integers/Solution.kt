// LeetCode 3886 - Sum of Sortable Integers
// https://leetcode.com/problems/sum-of-sortable-integers/

class Solution {
    fun rotationMatches(block: IntArray, target: IntArray): Boolean {
        val k = block.size
        val prefix = IntArray(k)
        for (i in 1 until k) {
            var j = prefix[i - 1]
            while (j > 0 && target[i] != target[j]) j = prefix[j - 1]
            if (target[i] == target[j]) j++
            prefix[i] = j
        }
        var matched = 0
        for (i in 0 until 2 * k - 1) {
            val x = block[i % k]
            while (matched > 0 && x != target[matched]) matched = prefix[matched - 1]
            if (x == target[matched]) matched++
            if (matched == k) return true
        }
        return false
    }

    fun sumOfSortableIntegers(nums: IntArray): Int {
        val n = nums.size
        val sorted = nums.clone()
        sorted.sort()
        val divisors = ArrayList<Int>()
        var d = 1
        while (d * d <= n) {
            if (n % d == 0) {
                divisors.add(d)
                if (d * d != n) divisors.add(n / d)
            }
            d++
        }
        var answer = 0
        for (k in divisors) {
            var ok = true
            var start = 0
            while (start < n) {
                val block = nums.copyOfRange(start, start + k)
                val target = sorted.copyOfRange(start, start + k)
                if (!rotationMatches(block, target)) {
                    ok = false
                    break
                }
                start += k
            }
            if (ok) answer += k
        }
        return answer
    }
}
