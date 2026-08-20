// LeetCode 1307 - Verbal Arithmetic Puzzle
// https://leetcode.com/problems/verbal-arithmetic-puzzle/

class Solution {
    func isSolvable(_ words: [String], _ result: String) -> Bool {
        if (words.map { $0.count }.max() ?? 0) > result.count { return false }
        if Set((words + [result]).joined()).count > 10 { return false }
        let leading = Set((words + [result]).compactMap { $0.count > 1 ? $0.first : nil })
        var value = [Character: Int]()
        var used = Array(repeating: false, count: 10)
        let width = result.count
        let wordChars = words.map { Array($0) }
        let resultChars = Array(result)
        func dfs(_ column: Int, _ row: Int, _ total: Int) -> Bool {
            if column == width { return total == 0 }
            if row < words.count {
                if column >= wordChars[row].count { return dfs(column, row + 1, total) }
                let ch = wordChars[row][wordChars[row].count - 1 - column]
                if let v = value[ch] { return dfs(column, row + 1, total + v) }
                for digit in 0..<10 {
                    if !used[digit] && (digit != 0 || !leading.contains(ch)) {
                        value[ch] = digit; used[digit] = true
                        if dfs(column, row + 1, total + digit) { return true }
                        used[digit] = false; value[ch] = nil
                    }
                }
                return false
            }
            let ch = resultChars[resultChars.count - 1 - column]
            let digit = total % 10, carry = total / 10
            if let v = value[ch] { return v == digit && dfs(column + 1, 0, carry) }
            if used[digit] || (digit == 0 && leading.contains(ch)) { return false }
            value[ch] = digit; used[digit] = true
            let ok = dfs(column + 1, 0, carry)
            used[digit] = false; value[ch] = nil
            return ok
        }
        return dfs(0, 0, 0)
    }
}
