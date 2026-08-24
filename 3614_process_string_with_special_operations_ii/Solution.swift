// LeetCode 3614 - Process String with Special Operations II
// https://leetcode.com/problems/process-string-with-special-operations-ii/

class Solution {
    func processStr(_ s: String, _ k0: Int) -> Character {
        var k = k0
        var m = 0
        for c in s {
            if c == "*" { m = m > 0 ? m - 1 : 0 }
            else if c == "#" { m <<= 1 }
            else if c != "%" { m += 1 }
        }
        if k >= m { return "." }
        let chars = Array(s)
        var i = chars.count - 1
        while true {
            let c = chars[i]
            if c == "*" { m += 1 }
            else if c == "#" {
                m /= 2
                if k >= m { k -= m }
            } else if c == "%" {
                k = m - 1 - k
            } else {
                m -= 1
                if k == m { return c }
            }
            i -= 1
        }
    }
}
