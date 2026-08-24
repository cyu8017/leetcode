// LeetCode 0984 - String Without AAA or BBB
// https://leetcode.com/problems/string-without-aaa-or-bbb/

class Solution {
    func strWithout3a3b(_ a: Int, _ b: Int) -> String {
        var a = a, b = b
        var ans = [Character]()
        while a > 0 || b > 0 {
            let writeA: Bool
            if ans.count >= 2 && ans[ans.count - 1] == ans[ans.count - 2] {
                writeA = ans[ans.count - 1] == "b"
            } else {
                writeA = a >= b
            }
            if writeA {
                ans.append("a")
                a -= 1
            } else {
                ans.append("b")
                b -= 1
            }
        }
        return String(ans)
    }
}
