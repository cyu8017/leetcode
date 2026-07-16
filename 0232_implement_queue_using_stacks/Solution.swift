// LeetCode 0232 - Implement Queue using Stacks
// https://leetcode.com/problems/implement-queue-using-stacks/

class MyQueue {
    private var inputStack = [Int]()
    private var outputStack = [Int]()

    private func move() {
        if outputStack.isEmpty {
            while !inputStack.isEmpty {
                outputStack.append(inputStack.removeLast())
            }
        }
    }

    func push(_ x: Int) {
        inputStack.append(x)
    }

    func pop() -> Int {
        move()
        return outputStack.removeLast()
    }

    func peek() -> Int {
        move()
        return outputStack.last!
    }

    func empty() -> Bool {
        return inputStack.isEmpty && outputStack.isEmpty
    }
}
