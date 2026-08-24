// LeetCode 2198 - Number of Single Divisor Triplets
// https://leetcode.com/problems/number-of-single-divisor-triplets/

class Solution {
    func singleDivisorTriplet(_ nums: [Int]) -> Int {
        var freq = [Int](repeating: 0, count: 101)
        for x in nums { freq[x] += 1 }
        var ans = 0
        for a in 1...100 where freq[a] > 0 {
            for b in a...100 where freq[b] > 0 {
                for c in b...100 where freq[c] > 0 {
                    let s = a + b + c
                    var cnt = 0
                    if s % a == 0 { cnt += 1 }
                    if s % b == 0 { cnt += 1 }
                    if s % c == 0 { cnt += 1 }
                    if cnt != 1 { continue }
                    if a == b && b == c {
                        ans += freq[a] * (freq[a] - 1) * (freq[a] - 2)
                    } else if a == b {
                        ans += freq[a] * (freq[a] - 1) * freq[c] * 3
                    } else if b == c {
                        ans += freq[b] * (freq[b] - 1) * freq[a] * 3
                    } else if a == c {
                        ans += freq[a] * (freq[a] - 1) * freq[b] * 3
                    } else {
                        ans += freq[a] * freq[b] * freq[c] * 6
                    }
                }
            }
        }
        return ans
    }
}
