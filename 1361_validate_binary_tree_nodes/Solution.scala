import scala.collection.mutable

object Solution {
  def validateBinaryTreeNodes(n: Int, leftChild: Array[Int], rightChild: Array[Int]): Boolean = {
    val indegree = Array.fill(n)(0)
    (leftChild ++ rightChild).foreach(x => if (x != -1) { indegree(x) += 1; if (indegree(x) > 1) return false })
    val roots = indegree.indices.filter(indegree(_) == 0)
    if (roots.length != 1) return false
    val seen = mutable.Set.empty[Int]; val stack = mutable.Stack(roots.head)
    while (stack.nonEmpty) { val node = stack.pop(); if (seen.contains(node)) return false; seen += node; Seq(leftChild(node), rightChild(node)).filter(_ != -1).foreach(stack.push) }
    seen.size == n
  }
}
