// LeetCode 0412 - Fizz Buzz

// https://leetcode.com/problems/fizz-buzz/



object Solution {

  def fizzBuzz(n: Int): List[String] = {

    (1 to n).map { value =>

      if (value % 15 == 0) "FizzBuzz"

      else if (value % 3 == 0) "Fizz"

      else if (value % 5 == 0) "Buzz"

      else value.toString

    }.toList

  }

}
