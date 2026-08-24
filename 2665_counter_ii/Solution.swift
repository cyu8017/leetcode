// LeetCode 2665 - Counter II
// https://leetcode.com/problems/counter-ii/

class CounterII {
    private let initVal: Int
    private var cur: Int

    init(_ initVal: Int) {
        self.initVal = initVal
        self.cur = initVal
    }

    func increment() -> Int {
        cur += 1
        return cur
    }

    func decrement() -> Int {
        cur -= 1
        return cur
    }

    func reset() -> Int {
        cur = initVal
        return cur
    }
}

class Solution {
    func createCounter(_ initVal: Int) -> CounterII {
        CounterII(initVal)
    }
}
