// LeetCode 3948 - Lexicographically Maximum MEX Array
// https://leetcode.com/problems/lexicographically-maximum-mex-array/


class Solution {
    func maxMexArray(_ nums: [Int]) -> [Int] {
        let n = nums.count
        var remaining = Array(repeating: 0, count: n + 2)
        for x in nums {
            if x <= n + 1 { remaining[x] += 1 }
        }
        var mex = 0
        while remaining[mex] > 0 { mex += 1 }
        var answer = [Int]()
        var seen = Array(repeating: 0, count: n + 2)
        var stamp = 0, index = 0
        while index < n {
            if mex == 0 {
                answer.append(0)
                let x = nums[index]
                if x <= n + 1 { remaining[x] -= 1 }
                index += 1
                continue
            }
            stamp += 1
            var need = mex
            while need > 0 {
                let x = nums[index]
                if x < mex && seen[x] != stamp {
                    seen[x] = stamp
                    need -= 1
                }
                if x <= n + 1 { remaining[x] -= 1 }
                index += 1
            }
            answer.append(mex)
            mex = 0
            while remaining[mex] > 0 { mex += 1 }
        }
        return answer
    }
}
