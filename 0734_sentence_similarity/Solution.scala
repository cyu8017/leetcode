// LeetCode 0734 - Sentence Similarity
// https://leetcode.com/problems/sentence-similarity/

object Solution {
  def areSentencesSimilar(sentence1: Array[String], sentence2: Array[String], similarPairs: List[List[String]]): Boolean = {
    if (sentence1.length != sentence2.length) return false
    val pairs = scala.collection.mutable.HashSet.empty[String]
    for (pair <- similarPairs) {
      pairs += pair(0) + "#" + pair(1)
      pairs += pair(1) + "#" + pair(0)
    }
    var i = 0
    while (i < sentence1.length) {
      if (sentence1(i) != sentence2(i) && !pairs.contains(sentence1(i) + "#" + sentence2(i))) return false
      i += 1
    }
    true
  }
}
