// LeetCode 0809 - Expressive Words
// https://leetcode.com/problems/expressive-words/

class Solution {
    func expressiveWords(_ s: String, _ words: [String]) -> Int {
        let target = groups(s)
        var ans = 0
        for word in words {
            let source = groups(word)
            if source.count != target.count { continue }
            var ok = true
            for i in 0..<source.count {
                if source[i].0 != target[i].0 { ok = false; break }
                let c1 = source[i].1, c2 = target[i].1
                if c1 > c2 || (c1 != c2 && c2 < 3) { ok = false; break }
            }
            if ok { ans += 1 }
        }
        return ans
    }

    private func groups(_ text: String) -> [(Character, Int)] {
        let chars = Array(text)
        var result = [(Character, Int)]()
        var i = 0
        while i < chars.count {
            var j = i
            while j < chars.count && chars[j] == chars[i] { j += 1 }
            result.append((chars[i], j - i))
            i = j
        }
        return result
    }
}
