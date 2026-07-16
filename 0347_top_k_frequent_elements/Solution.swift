// LeetCode 0347 - Top K Frequent Elements
// https://leetcode.com/problems/top-k-frequent-elements/

class Solution {
    func topKFrequent(_ nums: [Int], _ k: Int) -> [Int] {
        var counts: [Int: Int] = [:]
        for num in nums {
            counts[num, default: 0] += 1
        }

        var buckets = Array(repeating: [Int](), count: nums.count + 1)
        for (value, count) in counts {
            buckets[count].append(value)
        }

        var result: [Int] = []
        for index in stride(from: buckets.count - 1, through: 0, by: -1) {
            for value in buckets[index] {
                result.append(value)
                if result.count == k {
                    return result
                }
            }
        }

        return result
    }
}
