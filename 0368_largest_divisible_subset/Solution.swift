// LeetCode 0368 - Largest Divisible Subset
// https://leetcode.com/problems/largest-divisible-subset/

class Solution {
    func largestDivisibleSubset(_ nums: [Int]) -> [Int] {
        let sorted = nums.sorted()
        var chains: [Int: [Int]] = [:]
        for num in sorted {
            chains[num] = [num]
        }

        var best: [Int] = []
        for num in sorted {
            for (prev, chain) in chains {
                if prev < num && num % prev == 0 && chain.count + 1 > chains[num]!.count {
                    chains[num] = chain + [num]
                }
            }
            if chains[num]!.count > best.count {
                best = chains[num]!
            }
        }

        return best
    }
}
