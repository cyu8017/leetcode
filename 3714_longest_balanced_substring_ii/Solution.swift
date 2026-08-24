// LeetCode 3714 - Longest Balanced Substring II
// https://leetcode.com/problems/longest-balanced-substring-ii/

class Solution {
    func calc1(_ s: [Character]) -> Int {
        var res = 0
        let n = s.count
        var i = 0
        while i < n {
            var j = i + 1
            while j < n && s[j] == s[i] { j += 1 }
            res = max(res, j - i)
            i = j
        }
        return res
    }

    func calc2(_ s: [Character], _ a: Character, _ b: Character) -> Int {
        var res = 0
        let n = s.count
        var i = 0
        while i < n {
            while i < n && s[i] != a && s[i] != b { i += 1 }
            var pos = [0: i - 1]
            var d = 0
            while i < n && (s[i] == a || s[i] == b) {
                if s[i] == a { d += 1 } else { d -= 1 }
                if let p = pos[d] { res = max(res, i - p) }
                else { pos[d] = i }
                i += 1
            }
        }
        return res
    }

    func calc3(_ s: [Character]) -> Int {
        var pos = [Int: Int]()
        pos[0] = -1
        var cnt = [0, 0, 0]
        var res = 0
        for i in 0..<s.count {
            cnt[Int(s[i].asciiValue! - 97)] += 1
            let x = cnt[0] - cnt[1], y = cnt[1] - cnt[2]
            let k = (x << 32) ^ (y & 0xffffffff)
            if let p = pos[k] { res = max(res, i - p) }
            else { pos[k] = i }
        }
        return res
    }

    func longestBalanced(_ s: String) -> Int {
        let chars = Array(s)
        let x = calc1(chars)
        let y = max(calc2(chars, "a", "b"), max(calc2(chars, "b", "c"), calc2(chars, "a", "c")))
        let z = calc3(chars)
        return max(x, max(y, z))
    }
}
