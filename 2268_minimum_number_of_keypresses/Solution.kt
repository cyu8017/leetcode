// LeetCode 2268 - Minimum Number of Keypresses
// https://leetcode.com/problems/minimum-number-of-keypresses/

class Solution {

    fun minimumKeypresses(s: String): Int {

            var freq = IntArray(26)
            freq.fill(0)
            for (c in s.toCharArray()) freq[c - 'a']++
            freq.sortWith {  a, b  ->  Integer.compare(b, a })
            var ans = 0
            for (i in 0 until 26) {
                if (freq[i] == 0) break
                ans += freq[i] * (i / 9 + 1)
            }
            return ans

    }

}
