// LeetCode 3354 - Make Array Elements Equal to Zero
// https://leetcode.com/problems/make-array-elements-equal-to-zero/

class Solution {
    func countValidSelections(_ nums: [Int]) -> Int {
        let n = nums.count
        var ans = 0
        for i in 0..<n where nums[i] == 0 {
            for dir in [-1, 1] {
                var a = nums
                var cur = i, d = dir
                while cur >= 0 && cur < n {
                    if a[cur] == 0 { cur += d }
                    else {
                        a[cur] -= 1
                        d = -d
                        cur += d
                    }
                }
                if a.allSatisfy({ $0 == 0 }) { ans += 1 }
            }
        }
        return ans
    }
}
