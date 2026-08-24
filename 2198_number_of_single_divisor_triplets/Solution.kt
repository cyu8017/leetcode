// LeetCode 2198 - Number of Single Divisor Triplets
// https://leetcode.com/problems/number-of-single-divisor-triplets/

class Solution {

    fun singleDivisorTriplet(nums: IntArray): Long {

            var freq = LongArray(101)
            for (x in nums) freq[x]++
            var ans = 0
            for (a in 1..100) {
                if (freq[a] == 0) continue
                for (b in a..100) {
                    if (freq[b] == 0) continue
                    for (c in b..100) {
                        if (freq[c] == 0) continue
                        var s = a + b + c; var cnt = 0
                        if (s % a == 0) cnt++
                        if (s % b == 0) cnt++
                        if (s % c == 0) cnt++
                        if (cnt != 1) continue
                        if (a == b && b == c) ans += freq[a] * (freq[a] - 1) * (freq[a] - 2)
                        else if (a == b) ans += freq[a] * (freq[a] - 1) * freq[c] * 3
                        else if (b == c) ans += freq[b] * (freq[b] - 1) * freq[a] * 3
                        else if (a == c) ans += freq[a] * (freq[a] - 1) * freq[b] * 3
                        else ans += freq[a] * freq[b] * freq[c] * 6
                    }
                }
            }
            return ans

    }

}
