// LeetCode 0018 - 4Sum
// https://leetcode.com/problems/4sum/

class Solution {
    func fourSum(_ nums: [Int], _ target: Int) -> [[Int]] {
        let sorted = nums.sorted()
        var result: [[Int]] = []

        for i in 0..<(sorted.count - 3) {
            if i > 0 && sorted[i] == sorted[i - 1] {
                continue
            }

            for j in (i + 1)..<(sorted.count - 2) {
                if j > i + 1 && sorted[j] == sorted[j - 1] {
                    continue
                }

                var left = j + 1
                var right = sorted.count - 1
                while left < right {
                    let total = sorted[i] + sorted[j] + sorted[left] + sorted[right]
                    if total == target {
                        result.append([sorted[i], sorted[j], sorted[left], sorted[right]])
                        while left < right && sorted[left] == sorted[left + 1] {
                            left += 1
                        }
                        while left < right && sorted[right] == sorted[right - 1] {
                            right -= 1
                        }
                        left += 1
                        right -= 1
                    } else if total < target {
                        left += 1
                    } else {
                        right -= 1
                    }
                }
            }
        }

        return result
    }
}
