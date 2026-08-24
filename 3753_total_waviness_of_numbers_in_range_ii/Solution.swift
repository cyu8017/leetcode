// LeetCode 3753 - Total Waviness Of Numbers In Range II
// https://leetcode.com/problems/total-waviness-of-numbers-in-range-ii/

class Solution {
    private class Result {
        var count = 0
        var sum = 0
        init() {}
        init(_ c: Int, _ s: Int) { count = c; sum = s }
    }

    private func wavinessUpTo(_ limit: Int) -> Int {
        if limit < 0 { return 0 }
        var digits = [Int]()
        if limit == 0 {
            digits.append(0)
        } else {
            var value = limit
            while value > 0 {
                digits.append(value % 10)
                value /= 10
            }
            digits.reverse()
        }
        var memo = [String: Result]()
        return dfs(0, 10, 10, false, true, digits, &memo).sum
    }

    private func dfs(_ position: Int, _ secondLast: Int, _ last: Int, _ started: Bool, _ tight: Bool,
                     _ digits: [Int], _ memo: inout [String: Result]) -> Result {
        if position == digits.count { return Result(1, 0) }
        let key = "\(position),\(secondLast),\(last),\(started)"
        if !tight, let cached = memo[key] { return cached }
        let upper = tight ? digits[position] : 9
        let result = Result()
        for digit in 0...upper {
            let nextTight = tight && digit == upper
            var nextSecondLast = secondLast, nextLast = last
            let nextStarted = started || digit != 0
            var add = 0
            if !nextStarted {
                nextSecondLast = 10
                nextLast = 10
            } else if !started {
                nextSecondLast = 10
                nextLast = digit
            } else {
                if secondLast != 10 &&
                    ((last > secondLast && last > digit) || (last < secondLast && last < digit)) {
                    add = 1
                }
                nextSecondLast = last
                nextLast = digit
            }
            let child = dfs(position + 1, nextSecondLast, nextLast, nextStarted, nextTight, digits, &memo)
            result.count += child.count
            result.sum += child.sum + add * child.count
        }
        if !tight { memo[key] = result }
        return result
    }

    func totalWaviness(_ a: Int, _ b: Int) -> Int {
        return wavinessUpTo(b) - wavinessUpTo(a - 1)
    }
}
