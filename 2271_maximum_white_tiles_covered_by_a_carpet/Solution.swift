// LeetCode 2271 - Maximum White Tiles Covered by a Carpet
// https://leetcode.com/problems/maximum-white-tiles-covered-by-a-carpet/

class Solution {
    func maximumWhiteTiles(_ tiles: [[Int]], _ carpetLen: Int) -> Int {
        let tiles = tiles.sorted { $0[0] < $1[0] }
        let n = tiles.count
        var pref = [Int](repeating: 0, count: n + 1)
        for i in 0..<n { pref[i + 1] = pref[i] + (tiles[i][1] - tiles[i][0] + 1) }
        var ans = 0, j = 0
        for i in 0..<n {
            let end = tiles[i][0] + carpetLen - 1
            while j < n && tiles[j][0] <= end { j += 1 }
            var cover = pref[j] - pref[i]
            if j > 0 && tiles[j - 1][1] > end { cover -= tiles[j - 1][1] - end }
            ans = max(ans, cover)
        }
        return ans
    }
}
