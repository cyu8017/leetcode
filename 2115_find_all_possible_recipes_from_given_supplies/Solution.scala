// LeetCode 2115 - Find All Possible Recipes from Given Supplies
// https://leetcode.com/problems/find-all-possible-recipes-from-given-supplies/

object Solution {
  def findAllRecipes(recipes: Array[String], ingredients: List[List[String]], supplies: Array[String]): List[String] = {
    val have = scala.collection.mutable.Set(supplies.toSeq: _*)
    val indeg = scala.collection.mutable.Map.empty[String, Int]
    val graph = scala.collection.mutable.Map.empty[String, scala.collection.mutable.ArrayBuffer[String]]
    var i = 0
    while (i < recipes.length) {
      indeg(recipes(i)) = ingredients(i).size
      ingredients(i).foreach { ing =>
        graph.getOrElseUpdate(ing, scala.collection.mutable.ArrayBuffer.empty[String]) += recipes(i)
      }
      i += 1
    }
    val q = scala.collection.mutable.Queue[String]()
    have.foreach(q.enqueue)
    val ans = scala.collection.mutable.ArrayBuffer.empty[String]
    while (q.nonEmpty) {
      val cur = q.dequeue()
      if (graph.contains(cur)) {
        graph(cur).foreach { nxt =>
          indeg(nxt) = indeg(nxt) - 1
          if (indeg(nxt) == 0) {
            ans += nxt
            q.enqueue(nxt)
          }
        }
      }
    }
    ans.toList
  }
}
