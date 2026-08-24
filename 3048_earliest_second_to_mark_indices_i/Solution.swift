// LeetCode 3048 - Earliest Second to Mark Indices I
// https://leetcode.com/problems/earliest-second-to-mark-indices-i/

class Solution {
    private var nums: [Int] = []
    private var changeIndices: [Int] = []
    private var n = 0

    func earliestSecondToMarkIndices(_ nums: [Int], _ changeIndices: [Int]) -> Int {
        self.nums = nums
        self.changeIndices = changeIndices
        self.n = nums.count
        let m = changeIndices.count
        var l = 0, r = m + 1
        while l < r {
            let mid = (l + r) / 2
            if ok(mid) { r = mid }
            else { l = mid + 1 }
        }
        return l > m ? -1 : l
    }

    private func ok(_ t: Int) -> Bool {
        var last = Array(repeating: 0, count: n + 1)
        for s in 0..<t { last[changeIndices[s]] = s }
        var decrement = 0, marked = 0
        for s in 0..<t {
            let i = changeIndices[s]
            if last[i] == s {
                if decrement < nums[i - 1] { return false }
                decrement -= nums[i - 1]
                marked += 1
            } else {
                decrement += 1
            }
        }
        return marked == n
    }
}
