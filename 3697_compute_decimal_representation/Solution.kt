// LeetCode 3697 - Compute Decimal Representation
// https://leetcode.com/problems/compute-decimal-representation/

class Solution {
    fun decimalRepresentation(n: Int): IntArray {
        var ans = ArrayList<Int>()
        var p = 1
        while (n > 0) {
            var v = n % 10
            n /= 10
            if (v != 0) ans.add(p * v)
            p *= 10
        }
        ans.reverse()
        var res = IntArray(ans.size)
        for (i in 0 until ans.size) { res[i] = ans[i] }
        return res
    }
}
