// LeetCode 3866 - First Unique Even Element
// https://leetcode.com/problems/first-unique-even-element/

class Solution {
    func firstUniqueEven(_ nums: [Int]) -> Int {
        var cnt = [Int](repeating: 0, count: 101)
        for x in nums { cnt[x] += 1 }
        for x in nums {
            if x % 2 == 0 && cnt[x] == 1 { return x }
        }
        return -1
    }
}
