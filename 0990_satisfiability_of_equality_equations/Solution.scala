// LeetCode 0990 - Satisfiability of Equality Equations
// https://leetcode.com/problems/satisfiability-of-equality-equations/

object Solution {
  def equationsPossible(equations: Array[String]): Boolean = {
    val parent = Array.tabulate(26)(identity)
    def find(x: Int): Int = {
      if (parent(x) != x) parent(x) = find(parent(x))
      parent(x)
    }
    equations.foreach { eq =>
      if (eq.charAt(1) == '=') parent(find(eq.charAt(0) - 'a')) = find(eq.charAt(3) - 'a')
    }
    equations.forall { eq =>
      eq.charAt(1) != '!' || find(eq.charAt(0) - 'a') != find(eq.charAt(3) - 'a')
    }
  }
}
