// LeetCode 1343 - Number of Sub-arrays of Size K and Average Greater than or Equal to Threshold
// https://leetcode.com/problems/number-of-sub-arrays-of-size-k-and-average-greater-than-or-equal-to-threshold/

class Solution {
    func numOfSubarrays(_ arr: [Int], _ k: Int, _ threshold: Int) -> Int {
        var window = arr.prefix(k).reduce(0, +)
        var answer = window >= k * threshold ? 1 : 0
        for i in k..<arr.count {
            window += arr[i] - arr[i - k]
            if window >= k * threshold { answer += 1 }
        }
        return answer
    }
}
