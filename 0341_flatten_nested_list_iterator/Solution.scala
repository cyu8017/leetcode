// LeetCode 0341 - Flatten Nested List Iterator

// https://leetcode.com/problems/flatten-nested-list-iterator/



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

}



class NestedIterator(nestedList: List[NestedInteger]) {

  private case class Entry(node: NestedInteger, var index: Int)



  private val stack = mutable.ArrayDeque.empty[Entry]



  for (index <- nestedList.indices.reverse) {

    stack.append(Entry(nestedList(index), 0))

  }



  def next(): Int = {

    val current = stack.removeLast()

    if (current.node.isInteger()) {

      current.node.getInteger()

    } else {

      advance(current.node.getList())

    }

  }



  def hasNext(): Boolean = {

    prepareNext()

    stack.nonEmpty

  }



  private def prepareNext(): Unit = {

    while (stack.nonEmpty) {

      val top = stack.last

      val current = top.node

      if (current.isInteger()) {

        return

      }



      val nested = current.getList()

      if (top.index >= nested.length) {

        stack.removeLast()

      } else {

        top.index += 1

        stack.append(Entry(nested(top.index - 1), 0))

      }

    }

  }



  private def advance(nested: List[NestedInteger]): Int = {

    for (index <- nested.indices.reverse) {

      stack.append(Entry(nested(index), 0))

    }

    prepareNext()

    val current = stack.removeLast()

    if (current.node.isInteger()) {

      current.node.getInteger()

    } else {

      advance(current.node.getList())

    }

  }

}
