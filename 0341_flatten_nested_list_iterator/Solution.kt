// LeetCode 0341 - Flatten Nested List Iterator

// https://leetcode.com/problems/flatten-nested-list-iterator/



class NestedInteger {

    private var integer: Int? = null

    private val list = mutableListOf<NestedInteger>()



    constructor()



    constructor(value: Int) {

        integer = value

    }



    fun isInteger(): Boolean = integer != null



    fun getInteger(): Int = integer ?: 0



    fun getList(): List<NestedInteger> = list

}



class NestedIterator(nestedList: List<NestedInteger>) {

    private data class Entry(val node: NestedInteger, var index: Int)



    private val stack = ArrayDeque<Entry>()



    init {

        for (index in nestedList.indices.reversed()) {

            stack.addLast(Entry(nestedList[index], 0))

        }

    }



    fun next(): Int {

        val current = stack.removeLast()

        if (current.node.isInteger()) {

            return current.node.getInteger()

        }

        return advance(current.node.getList())

    }



    fun hasNext(): Boolean {

        prepareNext()

        return stack.isNotEmpty()

    }



    private fun prepareNext() {

        while (stack.isNotEmpty()) {

            val top = stack.last()

            val current = top.node

            if (current.isInteger()) {

                return

            }



            val nested = current.getList()

            if (top.index >= nested.size) {

                stack.removeLast()

                continue

            }



            top.index++

            stack.addLast(Entry(nested[top.index - 1], 0))

        }

    }



    private fun advance(nested: List<NestedInteger>): Int {

        for (index in nested.indices.reversed()) {

            stack.addLast(Entry(nested[index], 0))

        }

        prepareNext()

        val current = stack.removeLast()

        if (current.node.isInteger()) {

            return current.node.getInteger()

        }

        return advance(current.node.getList())

    }

}
