// LeetCode 0385 - Mini Parser

// https://leetcode.com/problems/mini-parser/



class NestedInteger {

    private var integer: Int? = null

    private val list = mutableListOf<NestedInteger>()



    constructor()



    constructor(value: Int) {

        integer = value

    }



    fun isInteger(): Boolean = integer != null



    fun getInteger(): Int = integer ?: 0



    fun getList(): MutableList<NestedInteger> = list

}



class Solution {

    fun deserialize(s: String): NestedInteger {

        if (s[0] != '[') {

            return NestedInteger(s.toInt())

        }



        val stack = ArrayDeque<NestedInteger>()

        var current: NestedInteger? = null

        var index = 0

        var negative = false

        var number = 0

        var hasNumber = false



        while (index < s.length) {

            when (val ch = s[index]) {

                '[' -> {

                    val item = NestedInteger()

                    if (current != null) {

                        stack.addLast(current)

                    }

                    current = item

                }

                '-' -> negative = true

                in '0'..'9' -> {

                    number = number * 10 + (ch - '0')

                    hasNumber = true

                }

                ',', ']' -> {

                    if (hasNumber) {

                        current!!.getList().add(NestedInteger(if (negative) -number else number))

                        number = 0

                        negative = false

                        hasNumber = false

                    }

                    if (ch == ']') {

                        if (stack.isEmpty()) {

                            return current!!

                        }

                        val parent = stack.removeLast()

                        parent.getList().add(current!!)

                        current = parent

                    }

                }

            }

            index++

        }



        return current ?: NestedInteger()

    }

}
