// LeetCode 0277 - Find the Celebrity
// https://leetcode.com/problems/find-the-celebrity/

def knows(a: Int, b: Int): Boolean = false

object Solution {
  def findCelebrity(n: Int): Int = {
    var candidate = 0
    for (person <- 1 until n) {
      if (knows(candidate, person)) {
        candidate = person
      }
    }
    for (person <- 0 until n if person != candidate) {
      if (knows(candidate, person) || !knows(person, candidate)) {
        return -1
      }
    }
    candidate
  }
}
