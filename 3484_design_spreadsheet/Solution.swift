// LeetCode 3484 - Design Spreadsheet
// https://leetcode.com/problems/design-spreadsheet/

class Spreadsheet {
    private var cells = [String: Int]()

    init(_ rows: Int) {}

    func setCell(_ cell: String, _ value: Int) { cells[cell] = value }

    func resetCell(_ cell: String) { cells.removeValue(forKey: cell) }

    func getValue(_ formula: String) -> Int {
        var formula = formula
        if !formula.isEmpty && formula.first == "=" { formula.removeFirst() }
        var sum = 0
        var start = formula.startIndex
        while start < formula.endIndex {
            let plus = formula[start...].firstIndex(of: "+")
            let p = plus == nil ? String(formula[start...]) : String(formula[start..<plus!])
            var isNum = !p.isEmpty && (p.first!.isNumber || (p.first == "-" && p.count > 1))
            if isNum {
                for ch in p.dropFirst() where !ch.isNumber { isNum = false; break }
            }
            if isNum { sum += Int(p) ?? 0 }
            else { sum += cells[p, default: 0] }
            if plus == nil { break }
            start = formula.index(after: plus!)
        }
        return sum
    }
}
