// LeetCode 1390 - Four Divisors
// https://leetcode.com/problems/four-divisors/

class Solution {
    func sumFourDivisors(_ nums: [Int]) -> Int {
        var ans = 0
        for x in nums {
            var ds = Set<Int>()
            let lim = Int(Double(x).squareRoot())
            for d in 1...max(lim, 1) {
                if x % d == 0 {
                    ds.insert(d); ds.insert(x / d)
                    if ds.count > 4 { break }
                }
            }
            if ds.count == 4 { ans += ds.reduce(0, +) }
        }
        return ans
    }
}
