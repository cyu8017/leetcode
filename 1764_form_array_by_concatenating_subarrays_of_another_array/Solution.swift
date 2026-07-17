// LeetCode 1764 - Form Array by Concatenating Subarrays of Another Array
// https://leetcode.com/problems/form-array-by-concatenating-subarrays-of-another-array/

class Solution {
    func canChoose(_ groups: [[Int]], _ nums: [Int]) -> Bool {
        let n = nums.count

        func matches(_ start: Int, _ g: [Int]) -> Bool {
            for t in 0..<g.count {
                if nums[start + t] != g[t] {
                    return false
                }
            }
            return true
        }

        func dfs(_ i: Int, _ start: Int) -> Bool {
            if i == groups.count {
                return start == n
            }
            let g = groups[i]
            let m = g.count
            if start > n - m {
                return false
            }
            for j in start...(n - m) {
                if matches(j, g) && dfs(i + 1, j + m) {
                    return true
                }
            }
            return false
        }

        return dfs(0, 0)
    }
}
