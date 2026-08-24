// LeetCode 0716 - Max Stack
// https://leetcode.com/problems/max-stack/

class MaxStack {
    private var stack = [Int]()
    private var maxStack = [Int]()

    init() {}

    func push(_ x: Int) {
        stack.append(x)
        maxStack.append(maxStack.last.map { max($0, x) } ?? x)
    }

    func pop() -> Int {
        maxStack.removeLast()
        return stack.removeLast()
    }

    func top() -> Int { stack.last! }

    func peekMax() -> Int { maxStack.last! }

    func popMax() -> Int {
        let m = peekMax()
        var buf = [Int]()
        while top() != m { buf.append(pop()) }
        _ = pop()
        for x in buf.reversed() { push(x) }
        return m
    }
}
