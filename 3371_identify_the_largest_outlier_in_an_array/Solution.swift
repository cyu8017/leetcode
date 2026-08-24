// LeetCode 3371 - Identify the Largest Outlier in an Array
// https://leetcode.com/problems/identify-the-largest-outlier-in-an-array/

class Solution {
    func getLargestOutlier(_ nums: [Int]) -> Int {
        var sum = 0
        var freq = [Int: Int]()
        for x in nums {
            sum += x
            freq[x, default: 0] += 1
        }
        var ans = Int.min
        for x in nums {
            freq[x]! -= 1
            let rem = sum - x
            if rem % 2 == 0 {
                let cand = rem / 2
                if freq[cand, default: 0] > 0 && x > ans { ans = x }
            }
            freq[x]! += 1
        }
        return ans
    }
}
