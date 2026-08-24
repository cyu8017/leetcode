// LeetCode 0913 - Cat and Mouse
// https://leetcode.com/problems/cat-and-mouse/

object Solution {
  def catMouseGame(graph: Array[Array[Int]]): Int = {
    val n = graph.length
    val DRAW = 0
    val MOUSE_WIN = 1
    val CAT_WIN = 2
    val states = Array.ofDim[Int](n, n, 2)
    val outDegree = Array.ofDim[Int](n, n, 2)
    val q = scala.collection.mutable.Queue[Array[Int]]()
    var cat = 0
    while (cat < n) {
      var mouse = 0
      while (mouse < n) {
        outDegree(cat)(mouse)(0) = graph(mouse).length
        var deg = 0
        graph(cat).foreach { x => if (x != 0) deg += 1 }
        outDegree(cat)(mouse)(1) = deg
        mouse += 1
      }
      cat += 1
    }
    cat = 1
    while (cat < n) {
      var move = 0
      while (move < 2) {
        states(cat)(0)(move) = MOUSE_WIN
        q.enqueue(Array(cat, 0, move, MOUSE_WIN))
        states(cat)(cat)(move) = CAT_WIN
        q.enqueue(Array(cat, cat, move, CAT_WIN))
        move += 1
      }
      cat += 1
    }
    while (q.nonEmpty) {
      val cur = q.dequeue()
      cat = cur(0)
      val mouse = cur(1)
      val move = cur(2)
      val state = cur(3)
      if (cat == 2 && mouse == 1 && move == 0) return state
      val prevMove = move ^ 1
      graph(if (prevMove == 1) cat else mouse).foreach { prev =>
        val prevCat = if (prevMove == 1) prev else cat
        if (prevCat != 0) {
          val prevMouse = if (prevMove == 1) mouse else prev
          if (states(prevCat)(prevMouse)(prevMove) == 0) {
            if ((prevMove == 0 && state == MOUSE_WIN) ||
                (prevMove == 1 && state == CAT_WIN) ||
                outDegree(prevCat)(prevMouse)(prevMove) == 1) {
              states(prevCat)(prevMouse)(prevMove) = state
              q.enqueue(Array(prevCat, prevMouse, prevMove, state))
            } else {
              outDegree(prevCat)(prevMouse)(prevMove) -= 1
            }
          }
        }
      }
    }
    states(2)(1)(0)
  }
}
