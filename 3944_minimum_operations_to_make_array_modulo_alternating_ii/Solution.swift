// LeetCode 3944 - Minimum Operations to Make Array Modulo Alternating II
// https://leetcode.com/problems/minimum-operations-to-make-array-modulo-alternating-ii/


class Solution {
    func minOperations(_ nums: [Int], _ k: Int) -> Int {
        var evenFreq = Array(repeating: 0, count: k)
        var oddFreq = Array(repeating: 0, count: k)
        for i in 0..<nums.count {
            if i % 2 == 0 { evenFreq[nums[i] % k] += 1 }
            else { oddFreq[nums[i] % k] += 1 }
        }
        let evenCost = costs(evenFreq, k)
        let oddCost = costs(oddFreq, k)
        var best1 = Int.max / 4, best2 = Int.max / 4
        var bestIndex = -1
        for i in 0..<k {
            let x = oddCost[i]
            if x < best1 {
                best2 = best1
                best1 = x
                bestIndex = i
            } else if x < best2 {
                best2 = x
            }
        }
        var ans = Int.max / 4
        for x in 0..<k {
            let other = (x == bestIndex) ? best2 : best1
            ans = min(ans, evenCost[x] + other)
        }
        return ans
    }

    private func costs(_ freq: [Int], _ k: Int) -> [Int] {
        var dbl = Array(repeating: 0, count: 2 * k)
        for i in 0..<(2 * k) { dbl[i] = freq[i % k] }
        var countPrefix = Array(repeating: 0, count: 2 * k + 1)
        var weightedPrefix = Array(repeating: 0, count: 2 * k + 1)
        for i in 0..<(2 * k) {
            countPrefix[i + 1] = countPrefix[i] + dbl[i]
            weightedPrefix[i + 1] = weightedPrefix[i] + i * dbl[i]
        }
        var res = Array(repeating: 0, count: k)
        let cw = k / 2, cc = (k - 1) / 2
        for t in 0..<k {
            let cnt = countPrefix[t + cw + 1] - countPrefix[t]
            let sum = weightedPrefix[t + cw + 1] - weightedPrefix[t]
            res[t] += sum - t * cnt
            if cc > 0 {
                let cnt2 = countPrefix[t + k] - countPrefix[t + k - cc]
                let sum2 = weightedPrefix[t + k] - weightedPrefix[t + k - cc]
                res[t] += (t + k) * cnt2 - sum2
            }
        }
        return res
    }
}
