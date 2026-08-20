// LeetCode 1122 - Relative Sort Array
// https://leetcode.com/problems/relative-sort-array/

class Solution {
    func relativeSortArray(_ arr1: [Int], _ arr2: [Int]) -> [Int] {
        var count: [Int: Int] = [:]
        for x in arr1 { count[x, default: 0] += 1 }
        var ans: [Int] = []
        for x in arr2 {
            if let c = count[x] {
                ans.append(contentsOf: repeatElement(x, count: c))
                count[x] = nil
            }
        }
        let rest = count.keys.sorted()
        for x in rest {
            ans.append(contentsOf: repeatElement(x, count: count[x]!))
        }
        return ans
    }
}
