// LeetCode 0315 - Count of Smaller Numbers After Self
// https://leetcode.com/problems/count-of-smaller-numbers-after-self/

class Solution {
    func countSmaller(_ nums: [Int]) -> [Int] {
        var sortedNums: [Int] = []
        var result: [Int] = []
        for num in nums.reversed() {
            let index = bisectLeft(sortedNums, num)
            result.append(index)
            sortedNums.insert(num, at: index)
        }
        return result.reversed()
    }

    private func bisectLeft(_ arr: [Int], _ num: Int) -> Int {
        var left = 0
        var right = arr.count
        while left < right {
            let mid = (left + right) / 2
            if arr[mid] < num {
                left = mid + 1
            } else {
                right = mid
            }
        }
        return left
    }
}
