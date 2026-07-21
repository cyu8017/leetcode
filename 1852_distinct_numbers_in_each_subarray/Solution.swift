// LeetCode 1852 - Distinct Numbers in Each Subarray
// https://leetcode.com/problems/distinct-numbers-in-each-subarray/

class Solution {
    func distinctNumbers(_ nums: [Int], _ k: Int) -> [Int] {
        var counts: [Int: Int] = [:]
        for i in 0..<k {
            counts[nums[i], default: 0] += 1
        }

        var result = [counts.count]
        var left = 0

        for right in k..<nums.count {
            counts[nums[right], default: 0] += 1
            let outgoing = nums[left]
            counts[outgoing, default: 0] -= 1
            if counts[outgoing] == 0 {
                counts.removeValue(forKey: outgoing)
            }
            left += 1
            result.append(counts.count)
        }

        return result
    }
}
