// LeetCode 0155 - Min Stack
// https://leetcode.com/problems/min-stack/

class MinStack {
    private var values: [Int] = []
    private var minimums: [Int] = []

    func push(_ val: Int) {
        values.append(val)
        minimums.append(min(val, minimums.last ?? val))
    }

    func pop() {
        values.removeLast()
        minimums.removeLast()
    }

    func top() -> Int {
        return values.last!
    }

    func getMin() -> Int {
        return minimums.last!
    }
}