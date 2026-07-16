// LeetCode 0385 - Mini Parser

// https://leetcode.com/problems/mini-parser/



import scala.collection.mutable



class NestedInteger {

  private var integer: Option[Int] = None

  private val list = mutable.ListBuffer.empty[NestedInteger]



  def this(value: Int) = {

    this()

    integer = Some(value)

  }



  def isInteger(): Boolean = integer.isDefined



  def getInteger(): Int = integer.getOrElse(0)



  def getList(): List[NestedInteger] = list.toList



  def appendItem(item: NestedInteger): Unit = list += item

}



object Solution {

  def deserialize(s: String): NestedInteger = {

    if (s(0) != '[') {

      return new NestedInteger(s.toInt)

    }



    val stack = mutable.Stack.empty[NestedInteger]

    var current: NestedInteger = null

    var index = 0

    var negative = false

    var number = 0

    var hasNumber = false



    while (index < s.length) {

      s(index) match {

        case '[' =>

          val item = new NestedInteger()

          if (current != null) {

            stack.push(current)

          }

          current = item

        case '-' => negative = true

        case ch if ch.isDigit =>

          number = number * 10 + (ch - '0')

          hasNumber = true

        case ',' | ']' =>

          if (hasNumber) {

            current.appendItem(new NestedInteger(if (negative) -number else number))

            number = 0

            negative = false

            hasNumber = false

          }

          if (s(index) == ']') {

            if (stack.isEmpty) {

              return current

            }

            val parent = stack.pop()

            parent.appendItem(current)

            current = parent

          }

        case _ =>

      }

      index += 1

    }



    if (current != null) current else new NestedInteger()

  }

}
