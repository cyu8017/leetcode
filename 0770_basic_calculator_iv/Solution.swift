// LeetCode 0770 - Basic Calculator IV
// https://leetcode.com/problems/basic-calculator-iv/

class Solution {
    func basicCalculatorIV(_ expression: String, _ evalvars: [String], _ evalints: [Int]) -> [String] {
        var values = [String: Int]()
        for i in 0..<evalvars.count { values[evalvars[i]] = evalints[i] }
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
        typealias Poly = [[String]: Int]
        func clean(_ poly: Poly) -> Poly { poly.filter { $0.value != 0 } }
        func add(_ left: Poly, _ right: Poly) -> Poly {
            var result = left
            for (k, v) in right { result[k, default: 0] += v }
            return clean(result)
        }
        func negate(_ poly: Poly) -> Poly {
            var result = Poly()
            for (k, v) in poly { result[k] = -v }
            return result
        }
        func mul(_ left: Poly, _ right: Poly) -> Poly {
            var result = Poly()
            for (lk, lv) in left {
                for (rk, rv) in right {
                    result[(lk + rk).sorted(), default: 0] += lv * rv
                }
            }
            return clean(result)
        }
        func atom(_ token: String) -> Poly {
            if token.first!.isLetter {
                if let v = values[token] { return [[:]: v].filter { $0.value != 0 } }
                return [[token]: 1]
            }
            return [[:]: Int(token)!]
        }
        func parseExpr() -> Poly {
            var poly = parseTerm()
            while pos < tokens.count && (tokens[pos] == "+" || tokens[pos] == "-") {
                let op = tokens[pos]
                pos += 1
                let right = parseTerm()
                poly = add(poly, op == "+" ? right : negate(right))
            }
            return poly
        }
        func parseTerm() -> Poly {
            var poly = parseFactor()
            while pos < tokens.count && tokens[pos] == "*" {
                pos += 1
                poly = mul(poly, parseFactor())
            }
            return poly
        }
        func parseFactor() -> Poly {
            if tokens[pos] == "(" {
                pos += 1
                let poly = parseExpr()
                pos += 1
                return poly
            }
            let t = tokens[pos]
            pos += 1
            return atom(t)
        }
        let poly = parseExpr()
        return poly.sorted { a, b in
            if a.key.count != b.key.count { return a.key.count > b.key.count }
            return a.key.lexicographicallyPrecedes(b.key)
        }.compactMap { key, val in
            if val == 0 { return nil }
            if key.isEmpty { return String(val) }
            return "\(val)*" + key.joined(separator: "*")
        }
    }
}
