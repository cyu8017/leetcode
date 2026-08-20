// LeetCode 1456 - Maximum Number of Vowels in a Substring of Given Length
// https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/

class Solution {
    func maxVowels(_ s: String, _ k: Int) -> Int {
        let vowels: Set<Character> = ["a","e","i","o","u"]
        let chars = Array(s)
        var cur = chars.prefix(k).filter { vowels.contains($0) }.count
        var ans = cur
        for i in k..<chars.count {
            if vowels.contains(chars[i]) { cur += 1 }
            if vowels.contains(chars[i - k]) { cur -= 1 }
            ans = max(ans, cur)
        }
        return ans
    }
}
