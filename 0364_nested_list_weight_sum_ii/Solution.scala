// LeetCode 0364 - Nested List Weight Sum II

// https://leetcode.com/problems/nested-list-weight-sum-ii/



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

  def depthSum(nestedList: List[NestedInteger]): Int = {

    val weighted = mutable.ArrayBuffer.empty[(Int, Int)]

    dfs(nestedList, 1, weighted)

    if (weighted.isEmpty) return 0



    val maxDepth = weighted.map(_._2).max

    weighted.map { case (value, depth) => value * (maxDepth - depth + 1) }.sum

  }



  private def dfs(items: List[NestedInteger], depth: Int, weighted: mutable.ArrayBuffer[(Int, Int)]): Unit = {

    for (item <- items) {

      if (item.isInteger()) {

        weighted += ((item.getInteger(), depth))

      } else {

        dfs(item.getList(), depth + 1, weighted)

      }

    }

  }

}
