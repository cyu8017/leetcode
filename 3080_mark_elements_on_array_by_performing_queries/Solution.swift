// LeetCode 3080 - Mark Elements on Array by Performing Queries
// https://leetcode.com/problems/mark-elements-on-array-by-performing-queries/

class Solution {
    func unmarkedSumArray(_ nums: [Int], _ queries: [[Int]]) -> [Int] {
        let n = nums.count
        var s = nums.reduce(0, +)
        var mark = Array(repeating: false, count: n)
        var arr = (0..<n).map { [nums[$0], $0] }
        arr.sort { a, b in a[0] != b[0] ? a[0] < b[0] : a[1] < b[1] }
        var ans = Array(repeating: 0, count: queries.count)
        var j = 0
        for qi in 0..<queries.count {
            let index = queries[qi][0]
            var k = queries[qi][1]
            if !mark[index] {
                mark[index] = true
                s -= nums[index]
            }
            while k > 0 && j < n {
                if !mark[arr[j][1]] {
                    mark[arr[j][1]] = true
                    s -= arr[j][0]
                    k -= 1
                }
                j += 1
            }
            ans[qi] = s
        }
        return ans
    }
}
