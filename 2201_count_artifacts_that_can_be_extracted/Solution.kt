// LeetCode 2201 - Count Artifacts That Can Be Extracted
// https://leetcode.com/problems/count-artifacts-that-can-be-extracted/

class Solution {

    fun digArtifacts(n: Int, artifacts: Array<IntArray>, dig: Array<IntArray>): Int {

            var dug = HashSet<Int>()
            for (d in dig) dug.add((d[0] << 32) | (d[1] & 0xffffffffL))
            var ans = 0
            for (a in artifacts) {
                var ok = true
                run { var r = a[0]; while (r <= a[2] && ok) { run { var c = a[1]; while (r++ } } c <= a[3]) { if (!dug.contains((r << 32) | (c & 0xffffffffL))) {
                            ok = false; c++ } }
                            break
                        }
                if (ok) ans++
            }
            return ans

    }

}
