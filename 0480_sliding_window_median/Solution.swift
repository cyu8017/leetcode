// LeetCode 0480 - Sliding Window Median
// https://leetcode.com/problems/sliding-window-median/

class Solution {
    private func bisectLeft(_ array: inout [Int], _ target: Int) -> Int {
        var left = 0
        var right = array.count
        while left < right {
            let mid = left + (right - left) / 2
            if array[mid] < target {
                left = mid + 1
            } else {
                right = mid
            }
        }
        return left
    }

    private func insertSorted(_ array: inout [Int], _ value: Int) {
        let position = bisectLeft(&array, value)
        array.insert(value, at: position)
    }

    func medianSlidingWindow(_ nums: [Int], _ k: Int) -> [Double] {
        var window = Array(nums.prefix(k)).sorted()
        var result: [Double] = []

        func appendMedian() {
            if k % 2 == 1 {
                result.append(Double(window[k / 2]))
            } else {
                result.append(Double(window[k / 2 - 1] + window[k / 2]) / 2.0)
            }
        }

        appendMedian()
        var index = k
        while index < nums.count {
            let outgoing = nums[index - k]
            let incoming = nums[index]
            let removeAt = bisectLeft(&window, outgoing)
            window.remove(at: removeAt)
            insertSorted(&window, incoming)
            appendMedian()
            index += 1
        }
        return result
    }
}
