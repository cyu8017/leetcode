// LeetCode 0414 - Third Maximum Number

// https://leetcode.com/problems/third-maximum-number/



object Solution {

  def thirdMax(nums: Array[Int]): Int = {

    var first: Option[Int] = None

    var second: Option[Int] = None

    var third: Option[Int] = None



    for (value <- nums) {

      if (first.contains(value) || second.contains(value) || third.contains(value)) {

        // skip duplicates

      } else if (first.isEmpty || value > first.get) {

        third = second

        second = first

        first = Some(value)

      } else if (second.isEmpty || value > second.get) {

        third = second

        second = Some(value)

      } else if (third.isEmpty || value > third.get) {

        third = Some(value)

      }

    }



    third.getOrElse(first.get)

  }

}
