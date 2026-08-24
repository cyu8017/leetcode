// LeetCode 2007 - Find Original Array From Doubled Array
// https://leetcode.com/problems/find-original-array-from-doubled-array/

class Solution {
    func findOriginalArray(_ changed: [Int]) -> [Int] {
        if changed.count % 2 != 0 { return [] }
        let sorted = changed.sorted()
        var freq = [Int: Int]()
        for x in sorted { freq[x, default: 0] += 1 }
        var ans = [Int]()
        for x in sorted {
            if freq[x, default: 0] == 0 { continue }
            freq[x]! -= 1
            if freq[2 * x, default: 0] == 0 { return [] }
            freq[2 * x]! -= 1
            ans.append(x)
        }
        return ans
    }
}
