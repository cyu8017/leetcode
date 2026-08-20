// LeetCode 1297 - Maximum Number of Occurrences of a Substring
// https://leetcode.com/problems/maximum-number-of-occurrences-of-a-substring/

class Solution {
    func maxFreq(_ s: String, _ maxLetters: Int, _ minSize: Int, _ maxSize: Int) -> Int {
        let chars = Array(s)
        var count: [String: Int] = [:]
        var ans = 0
        for i in 0...(chars.count - minSize) {
            let subArr = chars[i..<(i + minSize)]
            if Set(subArr).count <= maxLetters {
                let sub = String(subArr)
                count[sub, default: 0] += 1
                ans = max(ans, count[sub]!)
            }
        }
        return ans
    }
}
