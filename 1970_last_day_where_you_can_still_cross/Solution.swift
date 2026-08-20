// LeetCode 1970 - Last Day Where You Can Still Cross
// https://leetcode.com/problems/last-day-where-you-can-still-cross/

class Solution {
    func latestDayToCross(_ row: Int, _ col: Int, _ cells: [[Int]]) -> Int {
        func can(_ day: Int) -> Bool {
            var blocked = Set<Int>()
            for i in 0..<day {
                blocked.insert((cells[i][0] - 1) * col + (cells[i][1] - 1))
            }
            var stack: [Int] = []
            var seen = Set<Int>()
            for c in 0..<col {
                let id = c
                if !blocked.contains(id) {
                    stack.append(id)
                    seen.insert(id)
                }
            }
            while !stack.isEmpty {
                let id = stack.removeLast()
                let r = id / col, c = id % col
                if r == row - 1 { return true }
                for (nr, nc) in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)] {
                    if nr >= 0 && nr < row && nc >= 0 && nc < col {
                        let nid = nr * col + nc
                        if !blocked.contains(nid) && !seen.contains(nid) {
                            seen.insert(nid)
                            stack.append(nid)
                        }
                    }
                }
            }
            return false
        }
        var lo = 1, hi = cells.count, ans = 0
        while lo <= hi {
            let mid = (lo + hi) / 2
            if can(mid) {
                ans = mid
                lo = mid + 1
            } else {
                hi = mid - 1
            }
        }
        return ans
    }
}
