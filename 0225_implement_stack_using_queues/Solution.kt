// LeetCode 0225 - Implement Stack using Queues
// https://leetcode.com/problems/implement-stack-using-queues/

import java.util.ArrayDeque

class MyStack {
    private val queue = ArrayDeque<Int>()

    fun push(x: Int) {
        queue.addLast(x)
        repeat(queue.size - 1) {
            queue.addLast(queue.removeFirst())
        }
    }

    fun pop(): Int = queue.removeFirst()

    fun top(): Int = queue.first()

    fun empty(): Boolean = queue.isEmpty()
}
