// LeetCode 2964 - Number of Divisible Triplet Sums
// https://leetcode.com/problems/number-of-divisible-triplet-sums/

class Solution {
    func divisibleTripletCount(_ nums: [Int], _ d: Int) -> Int {
        let n = nums.count
        var ans = 0
        for i in 0..<n {
            var freq: [Int: Int] = [:]
            for j in (i + 1)..<n {
                let need = (d - (nums[i] + nums[j]) % d) % d
                ans += freq[need, default: 0]
                let key = nums[j] % d
                freq[key, default: 0] += 1
            }
        }
        return ans
    }
}
