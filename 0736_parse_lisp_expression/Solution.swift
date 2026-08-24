// LeetCode 0736 - Parse Lisp Expression
// https://leetcode.com/problems/parse-lisp-expression/

class Solution {
    func evaluate(_ expression: String) -> Int {
        var tokens = [String]()
        var cur = ""
        for ch in expression {
            if ch == "(" || ch == ")" {
                if !cur.isEmpty { tokens.append(cur); cur = "" }
                tokens.append(String(ch))
            } else if ch.isWhitespace {
                if !cur.isEmpty { tokens.append(cur); cur = "" }
            } else { cur.append(ch) }
        }
        if !cur.isEmpty { tokens.append(cur) }
        var pos = 0
        func parse(_ env: inout [[String: Int]]) -> Int {
            let token = tokens[pos]
            if token != "(" {
                pos += 1
                if token.first!.isNumber || (token.first == "-" && token.count > 1) { return Int(token)! }
                for i in stride(from: env.count - 1, through: 0, by: -1) {
                    if let v = env[i][token] { return v }
                }
                return 0
            }
            pos += 1
            let op = tokens[pos]
            pos += 1
            if op == "let" {
                env.append([:])
                while tokens[pos] != ")" {
                    if tokens[pos] == "(" || tokens[pos + 1] == ")" {
                        let value = parse(&env)
                        pos += 1
                        env.removeLast()
                        return value
                    }
                    let v = tokens[pos]
                    pos += 1
                    env[env.count - 1][v] = parse(&env)
                }
            }
            if op == "add" {
                let left = parse(&env), right = parse(&env)
                pos += 1
                return left + right
            }
            if op == "mult" {
                let left = parse(&env), right = parse(&env)
                pos += 1
                return left * right
            }
            return 0
        }
        var env = [[String: Int]]()
        return parse(&env)
    }
}
