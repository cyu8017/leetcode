// LeetCode 0351 - Android Unlock Patterns
// https://leetcode.com/problems/android-unlock-patterns/

class Solution {
    func numberOfPatterns(_ m: Int, _ n: Int) -> Int {
        let jumps: [String: Int] = [
            "0,2": 1, "2,0": 1,
            "0,6": 3, "6,0": 3,
            "0,8": 4, "8,0": 4,
            "2,8": 5, "8,2": 5,
            "2,6": 7, "6,2": 7,
            "6,8": 7, "8,6": 7,
            "1,7": 8, "7,1": 8,
            "3,7": 6, "7,3": 6,
            "1,5": 4, "5,1": 4,
            "3,5": 5, "5,3": 5,
            "1,3": 2, "3,1": 2,
            "4,5": 5, "5,4": 5,
            "4,7": 8, "7,4": 8,
            "4,3": 5, "3,4": 5,
            "4,1": 2, "1,4": 2,
            "4,6": 7, "6,4": 7,
            "4,8": 6, "8,4": 6,
            "4,0": 2, "0,4": 2,
            "4,2": 6, "2,4": 6,
        ]

        func isValid(_ visited: Int, _ last: Int, _ nextCell: Int) -> Bool {
            if visited & (1 << nextCell) != 0 {
                return false
            }

            let key = "\(last),\(nextCell)"
            if let middle = jumps[key] {
                return visited & (1 << middle) == 0
            }

            return abs(last / 3 - nextCell / 3) <= 1 && abs(last % 3 - nextCell % 3) <= 1
        }

        func dfs(_ visited: Int, _ last: Int, _ length: Int) -> Int {
            if length > n {
                return 0
            }

            var count = (m <= length && length <= n) ? 1 : 0
            for nextCell in 0..<9 where isValid(visited, last, nextCell) {
                count += dfs(visited | (1 << nextCell), nextCell, length + 1)
            }

            return count
        }

        return dfs(1 << 0, 0, 1) * 4
            + dfs(1 << 1, 1, 1) * 4
            + dfs(1 << 4, 4, 1)
    }
}
