// LeetCode 0282 - Expression Add Operators
// https://leetcode.com/problems/expression-add-operators/

class Solution {
    func addOperators(_ num: String, _ target: Int) -> [String] {
        var result: [String] = []
        let chars = Array(num)

        func backtrack(_ index: Int, _ path: String, _ value: Int, _ previous: Int) {
            if index == chars.count {
                if value == target {
                    result.append(path)
                }
                return
            }
            var end = index
            while end < chars.count {
                if end > index && chars[index] == "0" {
                    break
                }
                let currentStr = String(chars[index...end])
                let current = Int(currentStr)!
                if index == 0 {
                    backtrack(end + 1, currentStr, current, current)
                } else {
                    backtrack(end + 1, path + "+" + currentStr, value + current, current)
                    backtrack(end + 1, path + "-" + currentStr, value - current, -current)
                    backtrack(
                        end + 1,
                        path + "*" + currentStr,
                        value - previous + previous * current,
                        previous * current
                    )
                }
                end += 1
            }
        }

        backtrack(0, "", 0, 0)
        return result
    }
}
