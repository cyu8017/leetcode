// LeetCode 2418 - Sort the People
// https://leetcode.com/problems/sort-the-people/

object Solution {
  def sortPeople(names: Array[String], heights: Array[Int]): Array[String] = {
    val n = names.length
    val idx = Array.tabulate(n)(identity)
    scala.util.Sorting.stableSort(idx, (a: Int, b: Int) => heights(a) > heights(b))
    Array.tabulate(n)(i => names(idx(i)))
  }
}
