// LeetCode 1381 - Design a Stack With Increment Operation
// https://leetcode.com/problems/design-a-stack-with-increment-operation/

class CustomStack(private val maxSize: Int) {
    private val a = mutableListOf<Int>()

    fun push(x: Int) {
        if (a.size < maxSize) a.add(x)
    }

    fun pop(): Int = if (a.isEmpty()) -1 else a.removeAt(a.lastIndex)

    fun increment(k: Int, `val`: Int) {
        val n = minOf(k, a.size)
        for (i in 0 until n) a[i] += `val`
    }
}
