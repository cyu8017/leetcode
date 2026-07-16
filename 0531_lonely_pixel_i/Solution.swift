// LeetCode 0531 - Lonely Pixel I
// https://leetcode.com/problems/lonely-pixel-i/

class Solution {
    func findLonelyPixel(_ picture: [[Character]]) -> Int {
        let rows = picture.count
        let cols = picture[0].count
        let rowCounts = picture.map { $0.filter { $0 == "B" }.count }
        let colCounts = (0..<cols).map { c in
            (0..<rows).filter { picture[$0][c] == "B" }.count
        }

        var lonely = 0
        for r in 0..<rows {
            for c in 0..<cols {
                if picture[r][c] == "B" && rowCounts[r] == 1 && colCounts[c] == 1 {
                    lonely += 1
                }
            }
        }
        return lonely
    }
}
