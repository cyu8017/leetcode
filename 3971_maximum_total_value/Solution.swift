// LeetCode 3971 - Maximum Total Value
// https://leetcode.com/problems/maximum-total-value/


class Solution {
    func maximumTotalValue(_ value: [Int], _ decay: [Int], _ m: Int) -> Int {
        let mod = 1_000_000_007
        func countAtLeast(_ threshold: Int) -> Int {
            var count = 0
            for i in 0..<value.count {
                if value[i] >= threshold {
                    count += (value[i] - threshold) / decay[i] + 1
                }
            }
            return count
        }
        if countAtLeast(1) <= m {
            var sum = 0
            for i in 0..<value.count {
                let terms = (value[i] - 1) / decay[i] + 1
                sum = (sum + terms * value[i] - decay[i] * terms * (terms - 1) / 2) % mod
            }
            return sum
        }
        var high = 0
        for v in value { if v > high { high = v } }
        var low = 1
        while low < high {
            let mid = (low + high + 1) / 2
            if countAtLeast(mid) >= m { low = mid }
            else { high = mid - 1 }
        }
        let threshold = low
        var count = 0, sum = 0
        for i in 0..<value.count {
            if value[i] < threshold { continue }
            let terms = (value[i] - threshold) / decay[i] + 1
            count += terms
            sum = (sum + (terms * value[i] - decay[i] * terms * (terms - 1) / 2) % mod) % mod
        }
        sum = (sum - ((count - m) % mod) * (threshold % mod)) % mod
        if sum < 0 { sum += mod }
        return sum
    }
}
