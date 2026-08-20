// LeetCode 1985 - Find the Kth Largest Integer in the Array
// https://leetcode.com/problems/find-the-kth-largest-integer-in-the-array/

class Solution {
    func kthLargestNumber(_ nums: [String], _ k: Int) -> String {
        nums.sorted { a, b in
            if a.count != b.count { return a.count > b.count }
            return a > b
        }[k - 1]
    }
}
