// LeetCode 2601 - Prime Subtraction Operation
// https://leetcode.com/problems/prime-subtraction-operation/

class Solution {
    func primeSubOperation(_ nums: [Int]) -> Bool {
        let maxV = nums.max()!
        var isP = [Bool](repeating: true, count: maxV + 1)
        if maxV >= 0 { isP[0] = false }
        if maxV >= 1 { isP[1] = false }
        var i = 2
        while i * i <= maxV {
            if isP[i] {
                var j = i * i
                while j <= maxV {
                    isP[j] = false
                    j += i
                }
            }
            i += 1
        }
        var primes = [Int]()
        if maxV >= 2 {
            for p in 2...maxV where isP[p] { primes.append(p) }
        }
        var prev = 0
        for x in nums {
            let need = x - prev
            var best = -1
            for p in primes {
                if p >= need { break }
                best = p
            }
            let cur = best < 0 ? x : x - best
            if cur <= prev { return false }
            prev = cur
        }
        return true
    }
}
