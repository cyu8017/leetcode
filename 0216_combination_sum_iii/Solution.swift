// LeetCode 0216 - Combination Sum III
// https://leetcode.com/problems/combination-sum-iii/

class Solution {
    func combinationSum3(_ k: Int, _ n: Int) -> [[Int]] {
        var result: [[Int]] = []
        var path: [Int] = []

        func backtrack(_ start: Int, _ remaining: Int) {
            if path.count == k {
                if remaining == 0 {
                    result.append(path)
                }
                return
            }
            if remaining <= 0 || path.count >= k {
                return
            }

            for num in start...9 {
                if num > remaining {
                    break
                }
                path.append(num)
                backtrack(num + 1, remaining - num)
                path.removeLast()
            }
        }

        backtrack(1, n)
        return result
    }
}
