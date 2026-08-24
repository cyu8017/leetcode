// LeetCode 2704 - To Be Or Not To Be
// https://leetcode.com/problems/to-be-or-not-to-be/

class Expect(private val value: Int) {
  def toBe(other: Int): Boolean = {
    if (value == other) true
    else throw new RuntimeException("Not Equal")
  }

  def notToBe(other: Int): Boolean = {
    if (value != other) true
    else throw new RuntimeException("Equal")
  }
}

object Solution {
  def expect(`val`: Int): Expect = new Expect(`val`)
}
