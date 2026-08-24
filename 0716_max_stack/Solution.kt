// LeetCode 0716 - Max Stack
// https://leetcode.com/problems/max-stack/

class MaxStack {
    private val stack = ArrayList<Int>()
    private val maxes = ArrayList<Int>()

    fun push(x: Int) {
        stack.add(x)
        maxes.add(if (maxes.isEmpty()) x else maxOf(x, maxes[maxes.size - 1]))
    }

    fun pop(): Int {
        maxes.removeAt(maxes.size - 1)
        return stack.removeAt(stack.size - 1)
    }

    fun top(): Int = stack[stack.size - 1]

    fun peekMax(): Int = maxes[maxes.size - 1]

    fun popMax(): Int {
        val maxVal = peekMax()
        val buffer = ArrayList<Int>()
        while (top() != maxVal) buffer.add(pop())
        pop()
        for (i in buffer.size - 1 downTo 0) push(buffer[i])
        return maxVal
    }
}
