// LeetCode 3556 - Sum of Largest Prime Substrings
// https://leetcode.com/problems/sum-of-largest-prime-substrings/

class Solution {
    func isPrime(_ x: Int) -> Bool {
        if x < 2 { return false }
        var i = 2
        while i * i <= x {
            if x % i == 0 { return false }
            i += 1
        }
        return true
    }

    func sumOfLargestPrimes(_ s: String) -> Int {
        let chars = Array(s)
        var st = Set<Int>()
        let n = chars.count
        for i in 0..<n {
            var x = 0
            for j in i..<n {
                x = x * 10 + Int(chars[j].asciiValue! - 48)
                if isPrime(x) { st.insert(x) }
            }
        }
        var nums = Array(st).sorted()
        var ans = 0
        var i = nums.count - 1
        while i >= 0 && nums.count - i <= 3 {
            ans += nums[i]
            i -= 1
        }
        return ans
    }
}
