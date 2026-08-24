// LeetCode 0631 - Design Excel Sum Formula
// https://leetcode.com/problems/design-excel-sum-formula/

class Excel {
    private var values: [[Int]]
    private var formulas = [Int: [[Int]]]()

    init(_ height: Int, _ width: Character) {
        let cols = Int(width.asciiValue! - Character("A").asciiValue!) + 1
        values = Array(repeating: Array(repeating: 0, count: cols), count: height + 1)
    }

    func set(_ row: Int, _ column: Character, _ val: Int) {
        let col = Int(column.asciiValue! - Character("A").asciiValue!)
        formulas[key(row, col)] = nil
        values[row][col] = val
    }

    func get(_ row: Int, _ column: Character) -> Int {
        eval(row, Int(column.asciiValue! - Character("A").asciiValue!))
    }

    func sum(_ row: Int, _ column: Character, _ numbers: [String]) -> Int {
        let col = Int(column.asciiValue! - Character("A").asciiValue!)
        var cells = [[Int]]()
        for token in numbers {
            if let colon = token.firstIndex(of: ":") {
                let p1 = parse(String(token[..<colon]))
                let p2 = parse(String(token[token.index(after: colon)...]))
                for r in p1[0]...p2[0] {
                    for c in p1[1]...p2[1] {
                        cells.append([r, c])
                    }
                }
            } else {
                cells.append(parse(token))
            }
        }
        formulas[key(row, col)] = cells
        return eval(row, col)
    }

    private func parse(_ cell: String) -> [Int] {
        let arr = Array(cell)
        return [Int(String(arr[1...]))!, Int(arr[0].asciiValue! - Character("A").asciiValue!)]
    }

    private func eval(_ row: Int, _ col: Int) -> Int {
        if let formula = formulas[key(row, col)] {
            var total = 0
            for cell in formula { total += eval(cell[0], cell[1]) }
            return total
        }
        return values[row][col]
    }

    private func key(_ row: Int, _ col: Int) -> Int {
        (row << 16) | col
    }
}
