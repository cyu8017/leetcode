// LeetCode 3890 - Integers With Multiple Sum Of Two Cubes
// https://leetcode.com/problems/integers-with-multiple-sum-of-two-cubes/

class Solution {
    private static let GOOD: [Int] = {
        let LIMIT = 1_000_000_000
        var cnt = [Int: Int]()
        var cubes = [Int](repeating: 0, count: 1001)
        for i in 0...1000 { cubes[i] = i * i * i }
        for a in 1...1000 {
            for b in a...1000 {
                let x = cubes[a] + cubes[b]
                if x > LIMIT { break }
                cnt[x, default: 0] += 1
            }
        }
        return cnt.filter { $0.value > 1 }.map { $0.key }.sorted()
    }()

    func findGoodIntegers(_ n: Int) -> [Int] {
        var lo = 0, hi = Solution.GOOD.count
        while lo < hi {
            let mid = (lo + hi) / 2
            if Solution.GOOD[mid] <= n { lo = mid + 1 }
            else { hi = mid }
        }
        return Array(Solution.GOOD.prefix(lo))
    }
}
