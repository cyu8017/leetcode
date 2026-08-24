// LeetCode 2150 - Find All Lonely Numbers in the Array
// https://leetcode.com/problems/find-all-lonely-numbers-in-the-array/

class Solution {
    func findLonely(_ nums: [Int]) -> [Int] {
        var freq = [Int: Int]()
        for x in nums { freq[x, default: 0] += 1 }
        return freq.compactMap { kv in
            kv.value == 1 && freq[kv.key - 1] == nil && freq[kv.key + 1] == nil ? kv.key : nil
        }
    }
}
