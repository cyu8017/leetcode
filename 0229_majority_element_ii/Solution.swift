// LeetCode 0229 - Majority Element II
// https://leetcode.com/problems/majority-element-ii/

class Solution {
    func majorityElement(_ nums: [Int]) -> [Int] {
        var candidate1: Int? = nil
        var candidate2: Int? = nil
        var count1 = 0
        var count2 = 0

        for num in nums {
            if num == candidate1 {
                count1 += 1
            } else if num == candidate2 {
                count2 += 1
            } else if count1 == 0 {
                candidate1 = num
                count1 = 1
            } else if count2 == 0 {
                candidate2 = num
                count2 = 1
            } else {
                count1 -= 1
                count2 -= 1
            }
        }

        count1 = 0
        count2 = 0
        for num in nums {
            if num == candidate1 {
                count1 += 1
            } else if num == candidate2 {
                count2 += 1
            }
        }

        let threshold = nums.count / 3
        var result: [Int] = []
        if count1 > threshold {
            result.append(candidate1!)
        }
        if candidate2 != nil && candidate2 != candidate1 && count2 > threshold {
            result.append(candidate2!)
        }
        return result
    }
}
