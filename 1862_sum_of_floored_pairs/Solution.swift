// LeetCode 1862 - Sum of Floored Pairs
// https://leetcode.com/problems/sum-of-floored-pairs/

class Solution {
    func sumOfFlooredPairs(_ nums: [Int]) -> Int {
        let mod = 1_000_000_007
        let maxVal = nums.max() ?? 0
        var count = Array(repeating: 0, count: maxVal + 1)
        for num in nums {
            count[num] += 1
        }

        var prefix = Array(repeating: 0, count: maxVal + 1)
        prefix[0] = count[0]
        for value in 1...maxVal {
            prefix[value] = prefix[value - 1] + count[value]
        }

        var answer = 0
        for divisor in 1...maxVal {
            if count[divisor] == 0 { continue }
            var quotient = 1
            while quotient * divisor <= maxVal {
                let low = quotient * divisor
                let high = min((quotient + 1) * divisor - 1, maxVal)
                let matches = prefix[high] - (low > 0 ? prefix[low - 1] : 0)
                answer = (answer + count[divisor] * matches * quotient) % mod
                quotient += 1
            }
        }

        return answer
    }
}
