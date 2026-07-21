// LeetCode 1896 - Minimum Cost to Change the Final Value of Expression
// https://leetcode.com/problems/minimum-cost-to-change-the-final-value-of-expression/

class Solution {
    func minOperationsToFlip(_ expression: String) -> Int {
        let chars = Array(expression)
        var index = 0

        func combine(_ left: [Int], _ op: Character, _ right: [Int]) -> [Int] {
            let leftVal = left[0]
            let leftToZero = left[1]
            let leftToOne = left[2]
            let rightVal = right[0]
            let rightToZero = right[1]
            let rightToOne = right[2]

            if op == "&" {
                let andVal = leftVal & rightVal
                let andToZero = min(leftToZero, leftToOne + rightToZero)
                let andToOne = leftToOne + rightToOne
                let orToZero = leftToZero + rightToZero
                let orToOne = min(leftToOne, min(leftToZero + rightToOne, rightToZero + leftToOne))
                let val = andVal
                let toZero = min(andToZero, 1 + orToZero)
                let toOne = min(andToOne, 1 + orToOne)
                return [val, toZero, toOne]
            } else {
                let orVal = leftVal | rightVal
                let orToZero = leftToZero + rightToZero
                let orToOne = min(leftToOne, min(leftToZero + rightToOne, rightToZero + leftToOne))
                let andToZero = min(leftToZero, leftToOne + rightToZero)
                let andToOne = leftToOne + rightToOne
                let val = orVal
                let toZero = min(orToZero, 1 + andToZero)
                let toOne = min(orToOne, 1 + andToOne)
                return [val, toZero, toOne]
            }
        }

        func parseFactor() -> [Int] {
            if chars[index] == "0" || chars[index] == "1" {
                let value = Int(String(chars[index]))!
                index += 1
                let toZero = value == 0 ? 0 : 1
                let toOne = value == 0 ? 1 : 0
                return [value, toZero, toOne]
            }
            index += 1
            let node = parseExpr()
            index += 1
            return node
        }

        func parseExpr() -> [Int] {
            var node = parseFactor()
            while index < chars.count && (chars[index] == "&" || chars[index] == "|") {
                let op = chars[index]
                index += 1
                node = combine(node, op, parseFactor())
            }
            return node
        }

        let result = parseExpr()
        let value = result[0]
        let toZero = result[1]
        let toOne = result[2]
        return value == 0 ? toOne : toZero
    }
}
