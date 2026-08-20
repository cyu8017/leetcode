// LeetCode 1467 - Probability of a Two Boxes Having the Same Number of Distinct Balls
// https://leetcode.com/problems/probability-of-a-two-boxes-having-the-same-number-of-distinct-balls/

class Solution {
    func getProbability(_ balls: [Int]) -> Double {
        let half = balls.reduce(0, +) / 2
        var good = 0.0, total = 0.0
        func comb(_ n: Int, _ k: Int) -> Double {
            if k < 0 || k > n { return 0 }
            var res = 1.0
            for i in 0..<k { res *= Double(n - i); res /= Double(i + 1) }
            return res
        }
        func dfs(_ i: Int, _ left: Int, _ dl: Int, _ ways: Double) {
            if i == balls.count {
                if left == half {
                    total += ways
                    if dl == 0 { good += ways }
                }
                return
            }
            for x in 0...balls[i] where left + x <= half {
                dfs(i + 1, left + x, dl + (x > 0 ? 1 : 0) - (x < balls[i] ? 1 : 0),
                    ways * comb(balls[i], x))
            }
        }
        dfs(0, 0, 0, 1)
        return good / total
    }
}
