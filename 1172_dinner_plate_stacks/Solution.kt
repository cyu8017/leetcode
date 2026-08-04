// LeetCode 1172 - Dinner Plate Stacks
// https://leetcode.com/problems/dinner-plate-stacks/

import java.util.PriorityQueue

class DinnerPlates(private val capacity: Int) {
    private val stacks = mutableListOf<ArrayDeque<Int>>()
    private val available = PriorityQueue<Int>()

    fun push(`val`: Int) {
        while (available.isNotEmpty() && (available.peek() >= stacks.size || stacks[available.peek()].size == capacity)) {
            available.poll()
        }
        if (available.isEmpty()) {
            stacks.add(ArrayDeque())
            available.offer(stacks.size - 1)
        }
        val idx = available.peek()
        stacks[idx].addLast(`val`)
        if (stacks[idx].size == capacity) available.poll()
    }

    fun pop(): Int {
        while (stacks.isNotEmpty() && stacks.last().isEmpty()) stacks.removeAt(stacks.lastIndex)
        return if (stacks.isEmpty()) -1 else popAtStack(stacks.size - 1)
    }

    fun popAtStack(index: Int): Int {
        if (index < 0 || index >= stacks.size || stacks[index].isEmpty()) return -1
        if (stacks[index].size == capacity) available.offer(index)
        return stacks[index].removeLast()
    }
}
