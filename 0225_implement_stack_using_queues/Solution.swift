// LeetCode 0225 - Implement Stack using Queues
// https://leetcode.com/problems/implement-stack-using-queues/

class MyStack {
    private var queue = [Int]()

    func push(_ x: Int) {
        queue.append(x)
        if queue.count > 1 {
            for _ in 0..<(queue.count - 1) {
                queue.append(queue.removeFirst())
            }
        }
    }

    func pop() -> Int {
        return queue.removeFirst()
    }

    func top() -> Int {
        return queue[0]
    }

    func empty() -> Bool {
        return queue.isEmpty
    }
}
