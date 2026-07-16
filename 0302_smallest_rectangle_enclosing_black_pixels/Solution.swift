// LeetCode 0302 - Smallest Rectangle Enclosing Black Pixels
// https://leetcode.com/problems/smallest-rectangle-enclosing-black-pixels/

class Solution {
    func minArea(_ image: [[String]], _ x: Int, _ y: Int) -> Int {
        let rows = image.count
        let cols = image[0].count

        func columnHasBlack(_ col: Int) -> Bool {
            for row in 0..<rows where image[row][col] == "1" {
                return true
            }
            return false
        }

        func rowHasBlack(_ row: Int) -> Bool {
            for col in 0..<cols where image[row][col] == "1" {
                return true
            }
            return false
        }

        var left = 0
        var right = y
        while left < right {
            let mid = (left + right) / 2
            if columnHasBlack(mid) {
                right = mid
            } else {
                left = mid + 1
            }
        }
        let leftBound = left

        left = y
        right = cols - 1
        while left < right {
            let mid = (left + right + 1) / 2
            if columnHasBlack(mid) {
                left = mid
            } else {
                right = mid - 1
            }
        }
        let rightBound = left

        var top = 0
        var bottom = x
        while top < bottom {
            let mid = (top + bottom) / 2
            if rowHasBlack(mid) {
                bottom = mid
            } else {
                top = mid + 1
            }
        }
        let topBound = top

        top = x
        bottom = rows - 1
        while top < bottom {
            let mid = (top + bottom + 1) / 2
            if rowHasBlack(mid) {
                top = mid
            } else {
                bottom = mid - 1
            }
        }
        let bottomBound = top

        return (rightBound - leftBound + 1) * (bottomBound - topBound + 1)
    }
}
