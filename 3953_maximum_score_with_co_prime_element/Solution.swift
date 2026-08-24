// LeetCode 3953 - Maximum Score with Co-Prime Element
// https://leetcode.com/problems/maximum-score-with-co-prime-element/


class Solution {
    func maxScore(_ nums: [Int], _ maxVal: Int) -> Int {
        var limit = maxVal
        var frequency = Array(repeating: 0, count: 100001)
        for x in nums {
            frequency[x] += 1
            if x > limit { limit = x }
        }
        var divisible = Array(repeating: 0, count: limit + 1)
        for d in 1...limit {
            var multiple = d
            while multiple <= limit {
                if multiple < frequency.count { divisible[d] += frequency[multiple] }
                multiple += d
            }
        }
        var best = -nums.count
        var checked = Array(repeating: false, count: limit + 1)
        func badCount(_ x: Int) -> Int {
            var primes = [Int]()
            var y = x
            var p = 2
            while p * p <= y {
                if y % p == 0 {
                    primes.append(p)
                    while y % p == 0 { y /= p }
                }
                p += 1
            }
            if y > 1 { primes.append(y) }
            var bad = 0
            let psz = primes.count
            for mask in 1..<(1 << psz) {
                var product = 1, bits = 0
                for i in 0..<psz {
                    if ((mask >> i) & 1) != 0 {
                        product *= primes[i]
                        bits += 1
                    }
                }
                if bits % 2 == 1 { bad += divisible[product] }
                else { bad -= divisible[product] }
            }
            return bad
        }
        func evaluate(_ x: Int, _ exists: Bool) -> Int {
            if checked[x] { return Int.min / 4 }
            checked[x] = true
            let bad = badCount(x)
            let cost: Int
            if exists { cost = x > 1 ? bad - 1 : 0 }
            else { cost = bad > 0 ? bad : 1 }
            return x - cost
        }
        for x in 1...maxVal {
            best = max(best, evaluate(x, x < frequency.count && frequency[x] > 0))
        }
        for x in nums {
            best = max(best, evaluate(x, true))
        }
        return best
    }
}
