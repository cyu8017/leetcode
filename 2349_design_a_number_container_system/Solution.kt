// LeetCode 2349 - Design a Number Container System
// https://leetcode.com/problems/design-a-number-container-system/

import java.util.TreeSet

class NumberContainers {
    private val idx = HashMap<Int, Int>()
    private val heap = HashMap<Int, TreeSet<Int>>()

    fun change(index: Int, number: Int) {
        idx[index] = number
        heap.getOrPut(number) { TreeSet() }.add(index)
    }

    fun find(number: Int): Int {
        val h = heap[number] ?: return -1
        while (h.isNotEmpty()) {
            val i = h.first()
            if (idx[i] == number) return i
            h.pollFirst()
        }
        return -1
    }
}
