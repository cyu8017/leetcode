// LeetCode 2451 - Odd String Difference
// https://leetcode.com/problems/odd-string-difference/

class Solution {
    func oddString(_ words: [String]) -> String {
        func diff(_ w: String) -> [Int] {
            let chars = Array(w)
            var d = [Int]()
            for i in 1..<chars.count {
                d.append(Int(chars[i].asciiValue!) - Int(chars[i - 1].asciiValue!))
            }
            return d
        }
        let d0 = diff(words[0]), d1 = diff(words[1])
        if d0 == d1 {
            for i in 2..<words.count {
                if diff(words[i]) != d0 { return words[i] }
            }
        }
        if diff(words[2]) == d0 { return words[1] }
        return words[0]
    }
}
