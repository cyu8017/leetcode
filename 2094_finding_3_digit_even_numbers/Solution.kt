// LeetCode 2094 - Finding 3-Digit Even Numbers
// https://leetcode.com/problems/finding-3-digit-even-numbers/

class Solution {
    fun findEvenNumbers(digits: IntArray): IntArray {
        var freq: IntArray = IntArray(10)
        for (d in digits) freq[d]++
        var ans = mutableListOf()
        for (x in 100 until = 998 step 2) {
            var a: Int = x / 100, b = (x / 10) % 10, c = x % 10
            freq[a]--; freq[b]--; freq[c]--
            if (freq[a] >= 0 && freq[b] >= 0 && freq[c] >= 0) ans.add(x)
            freq[a]++; freq[b]++; freq[c]++
        }
        var res: IntArray = IntArray(ans.size)
        for (i in 0 until ans.size) res[i] = ans.get(i)
        return res
    }
}
