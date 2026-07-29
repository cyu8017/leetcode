// LeetCode 1066 - Campus Bikes II
// https://leetcode.com/problems/campus-bikes-ii/

class Solution {
    func assignBikes(_ workers: [[Int]], _ bikes: [[Int]]) -> Int {
        let m = bikes.count
        var memo = [Int: Int]()

        func dp(_ i: Int, _ mask: Int) -> Int {
            if i == workers.count { return 0 }
            let key = i * 1024 + mask
            if let cached = memo[key] { return cached }
            var best = Int.max
            let wx = workers[i][0], wy = workers[i][1]
            for b in 0..<m {
                if mask & (1 << b) != 0 { continue }
                let dist = abs(wx - bikes[b][0]) + abs(wy - bikes[b][1])
                best = min(best, dist + dp(i + 1, mask | (1 << b)))
            }
            memo[key] = best
            return best
        }

        return dp(0, 0)
    }
}
