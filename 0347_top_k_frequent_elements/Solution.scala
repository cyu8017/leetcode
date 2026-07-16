// LeetCode 0347 - Top K Frequent Elements

// https://leetcode.com/problems/top-k-frequent-elements/



import scala.collection.mutable



object Solution {

  def topKFrequent(nums: Array[Int], k: Int): Array[Int] = {

    val counts = mutable.Map.empty[Int, Int]

    for (num <- nums) {

      counts(num) = counts.getOrElse(num, 0) + 1

    }



    val buckets = Array.fill(nums.length + 1)(mutable.ListBuffer.empty[Int])

    for ((value, count) <- counts) {

      buckets(count) += value

    }



    val result = mutable.ArrayBuffer.empty[Int]

    for (index <- buckets.indices.reverse if result.size < k) {

      for (value <- buckets(index) if result.size < k) {

        result += value

      }

    }



    result.toArray

  }

}
