// LeetCode 1200 - Minimum Absolute Difference
// https://leetcode.com/problems/minimum-absolute-difference/

class Solution {
    func minimumAbsDifference(_ arr: [Int]) -> [[Int]] {
        let a = arr.sorted()
        var best = Int.max
        var ans: [[Int]] = []
        for i in 1..<a.count {
            let d = a[i] - a[i - 1]
            if d < best {
                best = d
                ans = [[a[i - 1], a[i]]]
            } else if d == best {
                ans.append([a[i - 1], a[i]])
            }
        }
        return ans
    }
}
