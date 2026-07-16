// LeetCode 0254 - Factor Combinations
// https://leetcode.com/problems/factor-combinations/

class Solution {
    func getFactors(_ n: Int) -> [[Int]] {
        var result: [[Int]] = []
        var path: [Int] = []

        func backtrack(_ remain: Int, _ start: Int) {
            if start > remain {
                if path.count > 1 {
                    result.append(path)
                }
                return
            }

            var factor = start
            while factor * factor <= remain {
                if remain % factor == 0 {
                    path.append(factor)
                    backtrack(remain / factor, factor)
                    path.removeLast()
                }
                factor += 1
            }

            if !path.isEmpty {
                path.append(remain)
                if path.count > 1 {
                    result.append(path)
                }
                path.removeLast()
            }
        }

        backtrack(n, 2)
        return result
    }
}
