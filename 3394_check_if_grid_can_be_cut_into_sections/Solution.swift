// LeetCode 3394 - Check if Grid can be Cut into Sections
// https://leetcode.com/problems/check-if-grid-can-be-cut-into-sections/

class Solution {
    func checkValidCuts(_ n: Int, _ rectangles: [[Int]]) -> Bool {
        return checkCut(rectangles, 0) || checkCut(rectangles, 1)
    }

    private func checkCut(_ rects: [[Int]], _ axis: Int) -> Bool {
        var arr = [[Int]]()
        for r in rects {
            if axis == 0 { arr.append([r[0], r[2]]) }
            else { arr.append([r[1], r[3]]) }
        }
        arr.sort { a, b in
            if a[0] == b[0] { return a[1] < b[1] }
            return a[0] < b[0]
        }
        var cuts = 0
        var end = arr[0][1]
        for i in 1..<arr.count {
            if arr[i][0] >= end {
                cuts += 1
                end = arr[i][1]
                if cuts >= 2 { return true }
            } else if arr[i][1] > end {
                end = arr[i][1]
            }
        }
        return false
    }
}
