// LeetCode 0339 - Nested List Weight Sum

// https://leetcode.com/problems/nested-list-weight-sum/



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



object Solution {

  def depthSum(nestedList: List[NestedInteger]): Int = dfs(nestedList, 1)



  private def dfs(items: List[NestedInteger], depth: Int): Int = {

    var total = 0

    for (item <- items) {

      if (item.isInteger()) {

        total += item.getInteger() * depth

      } else {

        total += dfs(item.getList(), depth + 1)

      }

    }

    total

  }

}
