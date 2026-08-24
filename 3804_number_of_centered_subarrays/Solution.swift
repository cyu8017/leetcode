// LeetCode 3804 - Number Of Centered Subarrays
// https://leetcode.com/problems/number-of-centered-subarrays/

class Solution {
    func centeredSubarrays(_ nums: [Int]) -> Int {
        let n = nums.count
        var ans = 0
        for i in 0..<n {
            var st = Set<Int>()
            var s = 0
            for j in i..<n {
                s += nums[j]
                st.insert(nums[j])
                if st.contains(s) { ans += 1 }
            }
        }
        return ans
    }
}
