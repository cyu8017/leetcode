// LeetCode 0368 - Largest Divisible Subset

// https://leetcode.com/problems/largest-divisible-subset/



import scala.collection.mutable



object Solution {

  def largestDivisibleSubset(nums: Array[Int]): List[Int] = {

    val sorted = nums.sorted

    val chains = mutable.Map.from(sorted.map(num => num -> mutable.ArrayBuffer(num)))

    var best = List.empty[Int]



    for (num <- sorted) {

      for (prev <- chains.keys) {

        if (prev < num && num % prev == 0 && chains(prev).length + 1 > chains(num).length) {

          chains(num) = chains(prev) ++ mutable.ArrayBuffer(num)

        }

      }

      if (chains(num).length > best.length) {

        best = chains(num).toList

      }

    }



    best

  }

}
