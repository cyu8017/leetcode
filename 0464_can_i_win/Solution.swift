// LeetCode 0464 - Can I Win
// https://leetcode.com/problems/can-i-win/

class Solution {
    private var memo: [Int: Bool] = [:]

    func canIWin(_ maxChoosableInteger: Int, _ desiredTotal: Int) -> Bool {
        if desiredTotal <= 0 {
            return true
        }
        let total = maxChoosableInteger * (maxChoosableInteger + 1) / 2
        if total < desiredTotal {
            return false
        }

        memo = [:]
        return canWin(state: 0, currentTotal: 0, maxChoosableInteger: maxChoosableInteger, desiredTotal: desiredTotal)
    }

    private func canWin(state: Int, currentTotal: Int, maxChoosableInteger: Int, desiredTotal: Int) -> Bool {
        if let cached = memo[state] {
            return cached
        }

        for pick in 1...maxChoosableInteger {
            let bit = 1 << (pick - 1)
            if (state & bit) != 0 {
                continue
            }
            if currentTotal + pick >= desiredTotal {
                memo[state] = true
                return true
            }
            if !canWin(state: state | bit, currentTotal: currentTotal + pick, maxChoosableInteger: maxChoosableInteger, desiredTotal: desiredTotal) {
                memo[state] = true
                return true
            }
        }

        memo[state] = false
        return false
    }
}
