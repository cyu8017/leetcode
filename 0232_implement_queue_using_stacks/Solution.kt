// LeetCode 0232 - Implement Queue using Stacks
// https://leetcode.com/problems/implement-queue-using-stacks/

class MyQueue {
    private val inputStack = ArrayDeque<Int>()
    private val outputStack = ArrayDeque<Int>()

    private fun move() {
        if (outputStack.isEmpty()) {
            while (inputStack.isNotEmpty()) {
                outputStack.addLast(inputStack.removeLast())
            }
        }
    }

    fun push(x: Int) {
        inputStack.addLast(x)
    }

    fun pop(): Int {
        move()
        return outputStack.removeLast()
    }

    fun peek(): Int {
        move()
        return outputStack.last()
    }

    fun empty(): Boolean {
        return inputStack.isEmpty() && outputStack.isEmpty()
    }
}
