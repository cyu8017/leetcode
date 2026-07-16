// LeetCode 0399 - Evaluate Division

// https://leetcode.com/problems/evaluate-division/



import scala.collection.mutable



object Solution {

  def calcEquation(

      equations: List[List[String]],

      values: Array[Double],

      queries: List[List[String]],

  ): Array[Double] = {

    val graph = mutable.Map.empty[String, mutable.Map[String, Double]]



    for (index <- equations.indices) {

      val dividend = equations(index)(0)

      val divisor = equations(index)(1)

      val value = values(index)

      graph.getOrElseUpdate(dividend, mutable.Map.empty[String, Double])(divisor) = value

      graph.getOrElseUpdate(divisor, mutable.Map.empty[String, Double])(dividend) = 1.0 / value

    }



    queries.map { query =>

      dfs(query(0), query(1), graph.toMap, mutable.Set.empty[String])

    }.toArray

  }



  private def dfs(

      start: String,

      end: String,

      graph: Map[String, Map[String, Double]],

      visited: mutable.Set[String],

  ): Double = {

    if (!graph.contains(start) || !graph.contains(end)) {

      return -1.0

    }

    if (start == end) {

      return 1.0

    }



    visited.add(start)

    for ((neighbor, weight) <- graph(start)) {

      if (!visited.contains(neighbor)) {

        val result = dfs(neighbor, end, graph, visited)

        if (result != -1.0) {

          return weight * result

        }

      }

    }



    -1.0

  }

}
