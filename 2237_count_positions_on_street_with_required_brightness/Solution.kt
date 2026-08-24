// LeetCode 2237 - Count Positions on Street With Required Brightness
// https://leetcode.com/problems/count-positions-on-street-with-required-brightness/

class Solution {

    fun meetRequirement(n: Int, lights: Array<IntArray>, requirement: IntArray): Int {

            var diff = IntArray(n + 1)
            for (light in lights) {
                var pos = light[0]; var r = light[1]
                var l = maxOf(0, pos - r)
                var rr = minOf(n - 1, pos + r)
                diff[l]++
                diff[rr + 1]--
            }
            var ans = 0; var cur = 0
            for (i in 0 until n) {
                cur += diff[i]
                if (cur >= requirement[i]) ans++
            }
            return ans

    }

}
