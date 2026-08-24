// LeetCode 2271 - Maximum White Tiles Covered by a Carpet
// https://leetcode.com/problems/maximum-white-tiles-covered-by-a-carpet/

class Solution {

    fun maximumWhiteTiles(tiles: Array<IntArray>, carpetLen: Int): Int {

            tiles.sortWith {  a, b  ->  Integer.compare(a[0], b[0] })
            var n = tiles.size
            var pref = IntArray(n + 1)
            for (i in 0 until n) { pref[i + 1] = pref[i] + (tiles[i][1] - tiles[i][0] + 1) }
            var ans = 0; var j = 0
            for (i in 0 until n) {
                var end = tiles[i][0] + carpetLen - 1
                while (j < n && tiles[j][0] <= end) j++
                var cover = pref[j] - pref[i]
                if (j > 0 && tiles[j - 1][1] > end) cover -= tiles[j - 1][1] - end
                ans = maxOf(ans, cover)
            }
            return ans

    }

}
