// LeetCode 2516 - Take K of Each Character From Left and Right
// https://leetcode.com/problems/take-k-of-each-character-from-left-and-right/

class Solution {
    func takeCharacters(_ s: String, _ k: Int) -> Int {
        let chars = Array(s)
        let n = chars.count
        var cnt = [Int](repeating: 0, count: 3)
        for c in chars {
            cnt[Int(c.asciiValue! - Character("a").asciiValue!)] += 1
        }
        if cnt[0] < k || cnt[1] < k || cnt[2] < k { return -1 }
        let need = [cnt[0] - k, cnt[1] - k, cnt[2] - k]
        var window = [Int](repeating: 0, count: 3)
        var left = 0, maxMid = 0
        for right in 0..<n {
            window[Int(chars[right].asciiValue! - Character("a").asciiValue!)] += 1
            while window[0] > need[0] || window[1] > need[1] || window[2] > need[2] {
                window[Int(chars[left].asciiValue! - Character("a").asciiValue!)] -= 1
                left += 1
            }
            maxMid = max(maxMid, right - left + 1)
        }
        return n - maxMid
    }
}
