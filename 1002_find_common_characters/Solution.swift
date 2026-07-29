// LeetCode 1002 - Find Common Characters
// https://leetcode.com/problems/find-common-characters/

class Solution {
    func commonChars(_ words: [String]) -> [String] {
        func count(_ s: String) -> [Int] {
            var c = Array(repeating: 0, count: 26)
            for ch in s.utf8 { c[Int(ch - 97)] += 1 }
            return c
        }
        var common = count(words[0])
        for w in words.dropFirst() {
            let cur = count(w)
            for i in 0..<26 { common[i] = min(common[i], cur[i]) }
        }
        var ans = [String]()
        for i in 0..<26 {
            let ch = String(Character(UnicodeScalar(97 + i)!))
            for _ in 0..<common[i] { ans.append(ch) }
        }
        return ans
    }
}
