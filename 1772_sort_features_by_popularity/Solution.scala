// LeetCode 1772 - Sort Features by Popularity
// https://leetcode.com/problems/sort-features-by-popularity/

object Solution {
  def sortFeatures(features: Array[String], responses: Array[String]): Array[String] = {
    val featureSet = features.toSet
    val count = scala.collection.mutable.Map.empty[String, Int].withDefaultValue(0)
    for (response <- responses) {
      val seen = response.split("\\s+").filter(featureSet.contains).toSet
      for (word <- seen) {
        count(word) += 1
      }
    }
    features.sortBy(f => (-count(f), f))
  }
}
