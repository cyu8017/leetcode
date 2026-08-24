// LeetCode 3159 - Find Occurrences of an Element in an Array
// https://leetcode.com/problems/find-occurrences-of-an-element-in-an-array/

class Solution {
    func occurrencesOfElement(_ nums: [Int], _ queries: [Int], _ x: Int) -> [Int] {
        var ids: [Int] = []
        for i in 0..<nums.count where nums[i] == x { ids.append(i) }
        return queries.map { i in i - 1 < ids.count ? ids[i - 1] : -1 }
    }
}
