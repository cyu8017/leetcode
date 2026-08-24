// LeetCode 0972 - Equal Rational Numbers
// https://leetcode.com/problems/equal-rational-numbers/

class Solution {
    func isRationalEqual(_ s: String, _ t: String) -> Bool {
        return abs(parse(s) - parse(t)) < 1e-12
    }

    private func parse(_ x: String) -> Double {
        if !x.contains("(") { return x.isEmpty ? 0.0 : Double(x)! }
        let lp = x.firstIndex(of: "(")!
        var nonRep = String(x[..<lp])
        let rp = x.index(before: x.endIndex)
        let rep = String(x[x.index(after: lp)..<rp])
        if !nonRep.contains(".") { nonRep += "." }
        let dot = nonRep.firstIndex(of: ".")!
        let integer = String(nonRep[..<dot])
        let frac = String(nonRep[nonRep.index(after: dot)...])
        var bas = integer.isEmpty ? 0.0 : Double(integer)!
        if !frac.isEmpty {
            var denom = 1.0
            for _ in 0..<frac.count { denom *= 10 }
            bas += Double(frac)! / denom
        }
        if !rep.isEmpty {
            let repVal = Double(rep)!
            var cycle = 1.0
            for _ in 0..<rep.count { cycle *= 10 }
            var denom = cycle - 1
            for _ in 0..<frac.count { denom *= 10 }
            bas += repVal / denom
        }
        return bas
    }
}
