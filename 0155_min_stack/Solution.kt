import java.util.ArrayDeque

class MinStack {
    private val stack = ArrayDeque<Int>()
    private val minimums = ArrayDeque<Int>()
    fun push(`val`: Int) { stack.addLast(`val`); minimums.addLast(if (minimums.isEmpty()) `val` else minOf(`val`, minimums.last())) }
    fun pop() { stack.removeLast(); minimums.removeLast() }
    fun top(): Int = stack.last()
    fun getMin(): Int = minimums.last()
}