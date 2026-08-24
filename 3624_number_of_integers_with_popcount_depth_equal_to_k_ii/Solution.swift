// LeetCode 3624 - Number of Integers With Popcount Depth Equal to K II
// https://leetcode.com/problems/number-of-integers-with-popcount-depth-equal-to-k-ii/

class Solution {
    func depth(_ x0: Int) -> Int {
        if x0 == 1 { return 0 }
        var x = x0, d = 0
        while x > 1 {
            x = x.nonzeroBitCount
            d += 1
        }
        return d
    }

    func popcountDepth(_ nums: [Int], _ queries: [[Int]]) -> [Int] {
        var a = nums
        var ans = [Int]()
        for q in queries {
            if q[0] == 1 {
                let l = q[1], r = q[2], k = q[3]
                var cnt = 0
                for i in l...r where depth(a[i]) == k { cnt += 1 }
                ans.append(cnt)
            } else {
                a[q[1]] = q[2]
            }
        }
        return ans
    }
}
