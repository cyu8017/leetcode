// LeetCode 3526 - Range XOR Queries with Subarray Reversals
// https://leetcode.com/problems/range-xor-queries-with-subarray-reversals/

class Solution {
    func getResults(_ nums: [Int], _ queries: [[Int]]) -> [Int] {
        var a = nums
        var ans = [Int]()
        for q in queries {
            let typ = q[0]
            if typ == 1 {
                var l = q[1], r = q[2]
                while l < r {
                    let tmp = a[l]; a[l] = a[r]; a[r] = tmp
                    l += 1; r -= 1
                }
            } else if typ == 2 {
                let l = q[1], r = q[2]
                var x = 0
                for i in l...r { x ^= a[i] }
                ans.append(x)
            } else {
                a[q[1]] = q[2]
            }
        }
        return ans
    }
}
