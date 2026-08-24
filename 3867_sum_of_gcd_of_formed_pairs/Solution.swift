// LeetCode 3867 - Sum Of Gcd Of Formed Pairs
// https://leetcode.com/problems/sum-of-gcd-of-formed-pairs/

class Solution {
    private func gcd(_ a: Int, _ b: Int) -> Int {
        var a = a, b = b
        while b != 0 {
            let t = a % b
            a = b
            b = t
        }
        return a
    }

    func gcdSum(_ nums: [Int]) -> Int {
        let n = nums.count
        var prefixGcd = [Int](repeating: 0, count: n)
        var mx = 0
        for i in 0..<n {
            mx = max(mx, nums[i])
            prefixGcd[i] = gcd(nums[i], mx)
        }
        prefixGcd.sort()
        var ans = 0
        for i in 0..<(n / 2) { ans += gcd(prefixGcd[i], prefixGcd[n - i - 1]) }
        return ans
    }
}
