// LeetCode 1258 - Synonymous Sentences
// https://leetcode.com/problems/synonymous-sentences/

object Solution {
  def generateSentences(synonyms: List[List[String]], text: String): List[String] = {
    val parent = scala.collection.mutable.Map.empty[String, String]
    def find(x: String): String = {
      parent.getOrElseUpdate(x, x)
      if (parent(x) != x) parent(x) = find(parent(x))
      parent(x)
    }
    for (pair <- synonyms) {
      val ra = find(pair(0))
      val rb = find(pair(1))
      parent(ra) = rb
    }
    val groups = scala.collection.mutable.Map.empty[String, scala.collection.mutable.ListBuffer[String]]
    for (word <- parent.keys) {
      groups.getOrElseUpdate(find(word), scala.collection.mutable.ListBuffer.empty) += word
    }
    val words = text.split(" ")
    val choices = words.map { w =>
      if (parent.contains(w)) groups(find(w)).sorted.toList else List(w)
    }
    def product(idx: Int, cur: List[String], acc: scala.collection.mutable.ListBuffer[String]): Unit = {
      if (idx == choices.length) acc += cur.reverse.mkString(" ")
      else for (w <- choices(idx)) product(idx + 1, w :: cur, acc)
    }
    val acc = scala.collection.mutable.ListBuffer.empty[String]
    product(0, Nil, acc)
    acc.toList.sorted
  }
}
