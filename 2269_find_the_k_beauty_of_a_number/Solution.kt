// LeetCode 2269 - Find the K-Beauty of a Number
// https://leetcode.com/problems/find-the-k-beauty-of-a-number/

class Solution {

    fun divisorSubstrings(num: Int, k: Int): Int {

            var s = Integer.toString(num)
            var ans = 0
            run {
    var i = 0
    while (i + k <= s.length) {

                var sub = 0
                for (j in 0 until k) { sub = sub * 10 + (s[i + j] - '0') }
                if (sub != 0 && num % sub == 0) ans++

    i++
    }
    }
            return ans

    }

}
