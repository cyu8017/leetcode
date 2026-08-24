// LeetCode 2950 - Number of Divisible Substrings
// https://leetcode.com/problems/number-of-divisible-substrings/

class Solution {
    func countDivisibleSubstrings(_ word: String) -> Int {
        let vals = [1,1,2,2,2,3,3,3,4,4,4,5,5,5,6,6,6,7,7,7,8,8,8,9,9,9]
        let chars = Array(word)
        var ans = 0
        for i in 0..<chars.count {
            var sum = 0
            for j in i..<chars.count {
                sum += vals[Int(chars[j].asciiValue! - Character("a").asciiValue!)]
                if sum % (j - i + 1) == 0 { ans += 1 }
            }
        }
        return ans
    }
}
