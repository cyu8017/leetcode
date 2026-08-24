// LeetCode 3843 - First Element With Unique Frequency
// https://leetcode.com/problems/first-element-with-unique-frequency/

class Solution {
    func firstUniqueFreq(_ nums: [Int]) -> Int {
        var cnt = [Int: Int]()
        for x in nums { cnt[x, default: 0] += 1 }
        var freq = [Int: Int]()
        for v in cnt.values { freq[v, default: 0] += 1 }
        for x in nums {
            if freq[cnt[x]!] == 1 { return x }
        }
        return -1
    }
}
