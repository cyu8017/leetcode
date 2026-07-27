// LeetCode 1600 - Throne Inheritance
// https://leetcode.com/problems/throne-inheritance/

import scala.collection.mutable

class ThroneInheritance(_kingName: String) {
  private val king = _kingName
  private val children = mutable.Map.empty[String, mutable.ArrayBuffer[String]]
  private val dead = mutable.Set.empty[String]

  def birth(parentName: String, childName: String): Unit = {
    children.getOrElseUpdate(parentName, mutable.ArrayBuffer.empty) += childName
  }

  def death(name: String): Unit = { dead += name }

  def getInheritanceOrder(): List[String] = {
    val order = mutable.ArrayBuffer.empty[String]
    def visit(name: String): Unit = {
      if (!dead.contains(name)) order += name
      children.getOrElse(name, mutable.ArrayBuffer.empty).foreach(visit)
    }
    visit(king)
    order.toList
  }
}
