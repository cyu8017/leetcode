// LeetCode 0323 - Number of Connected Components in an Undirected Graph

// https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/



object Solution {

  def countComponents(n: Int, edges: Array[Array[Int]]): Int = {

    val parent = Array.tabulate(n)(identity)

    val rank = new Array[Int](n)

    var components = n

    for (edge <- edges) {

      val left = edge(0)

      val right = edge(1)

      var rootLeft = find(parent, left)

      var rootRight = find(parent, right)

      if (rootLeft == rootRight) {

        // already connected

      } else {

        if (rank(rootLeft) < rank(rootRight)) {

          val temp = rootLeft

          rootLeft = rootRight

          rootRight = temp

        }

        parent(rootRight) = rootLeft

        if (rank(rootLeft) == rank(rootRight)) {

          rank(rootLeft) += 1

        }

        components -= 1

      }

    }

    components

  }



  private def find(parent: Array[Int], node: Int): Int = {

    if (parent(node) != node) {

      parent(node) = find(parent, parent(node))

    }

    parent(node)

  }

}

