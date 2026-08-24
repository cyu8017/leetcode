// LeetCode 0957 - Prison Cells After N Days
// https://leetcode.com/problems/prison-cells-after-n-days/

class Solution {
    func prisonAfterNDays(_ cells: [Int], _ n: Int) -> [Int] {
        var seen = [String: Int]()
        var state = cells
        var n = n
        while n > 0 {
            let key = state.map(String.init).joined(separator: ",")
            if let prev = seen[key] {
                let cycle = prev - n
                if cycle > 0 { n %= cycle }
                if n == 0 { break }
            }
            seen[key] = n
            var nxt = Array(repeating: 0, count: 8)
            for i in 1...6 { nxt[i] = state[i - 1] == state[i + 1] ? 1 : 0 }
            state = nxt
            n -= 1
        }
        return state
    }
}
