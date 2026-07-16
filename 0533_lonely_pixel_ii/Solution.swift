// LeetCode 0533 - Lonely Pixel II
// https://leetcode.com/problems/lonely-pixel-ii/

class Solution {
    func findBlackPixel(_ picture: [[Character]], _ target: Int) -> Int {
        let rows = picture.count
        let cols = picture[0].count
        let rowStrings = picture.map { String($0) }
        let rowCounts = picture.map { $0.filter { $0 == "B" }.count }
        let colCounts = (0..<cols).map { c in
            (0..<rows).filter { picture[$0][c] == "B" }.count
        }

        var lonely = 0
        for r in 0..<rows {
            if rowCounts[r] != target {
                continue
            }
            for c in 0..<cols {
                if picture[r][c] != "B" || colCounts[c] != target {
                    continue
                }
                let matches = (0..<rows).allSatisfy { i in
                    picture[i][c] != "B" || rowStrings[r] == rowStrings[i]
                }
                if matches {
                    lonely += 1
                }
            }
        }
        return lonely
    }
}
