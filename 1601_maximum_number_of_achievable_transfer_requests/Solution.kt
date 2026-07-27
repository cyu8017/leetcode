// LeetCode 1601 - Maximum Number of Achievable Transfer Requests
// https://leetcode.com/problems/maximum-number-of-achievable-transfer-requests/

class Solution {
    fun maximumRequests(n: Int, requests: Array<IntArray>): Int {
        val m = requests.size
        var ans = 0
        for (mask in 0 until (1 shl m)) {
            val bits = Integer.bitCount(mask)
            if (bits <= ans) continue
            val bal = IntArray(n)
            for (i in 0 until m) {
                if ((mask shr i) and 1 == 1) {
                    bal[requests[i][0]]--
                    bal[requests[i][1]]++
                }
            }
            if (bal.all { it == 0 }) ans = bits
        }
        return ans
    }
}
