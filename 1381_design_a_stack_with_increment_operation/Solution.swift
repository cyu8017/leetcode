// LeetCode 1381 - Design a Stack With Increment Operation
// https://leetcode.com/problems/design-a-stack-with-increment-operation/

class CustomStack {
    private let maxSize: Int
    private var a = [Int]()

    init(_ maxSize: Int) { self.maxSize = maxSize }

    func push(_ x: Int) {
        if a.count < maxSize { a.append(x) }
    }

    func pop() -> Int { a.isEmpty ? -1 : a.removeLast() }

    func increment(_ k: Int, _ val: Int) {
        for i in 0..<min(k, a.count) { a[i] += val }
    }
}
