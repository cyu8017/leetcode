// LeetCode 3602 - Hexadecimal and Hexatrigesimal Conversion
// https://leetcode.com/problems/hexadecimal-and-hexatrigesimal-conversion/

class Solution {
    func f(_ x0: Int, _ k: Int) -> String {
        var x = x0
        var res = [Character]()
        while x > 0 {
            let v = x % k
            if v <= 9 { res.append(Character(UnicodeScalar(48 + v)!)) }
            else { res.append(Character(UnicodeScalar(65 + v - 10)!)) }
            x /= k
        }
        return String(res.reversed())
    }

    func concatHex36(_ n: Int) -> String {
        return f(n * n, 16) + f(n * n * n, 36)
    }
}
