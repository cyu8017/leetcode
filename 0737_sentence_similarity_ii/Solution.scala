// LeetCode 0737 - Sentence Similarity II
// https://leetcode.com/problems/sentence-similarity-ii/

object Solution {
  def areSentencesSimilarTwo(sentence1: Array[String], sentence2: Array[String], similarPairs: List[List[String]]): Boolean = {
    if (sentence1.length != sentence2.length) return false
    val parent = scala.collection.mutable.HashMap.empty[String, String]
    def find(x0: String): String = {
      parent.getOrElseUpdate(x0, x0)
      var x = x0
      while (parent(x) != x) {
        parent(x) = parent(parent(x))
        x = parent(x)
      }
      x
    }
    def unite(a: String, b: String): Unit = { parent(find(a)) = find(b) }
    for (pair <- similarPairs) unite(pair(0), pair(1))
    var i = 0
    while (i < sentence1.length) {
      if (find(sentence1(i)) != find(sentence2(i))) return false
      i += 1
    }
    true
  }
}
