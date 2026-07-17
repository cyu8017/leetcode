// LeetCode 1728 - Cat and Mouse II
// https://leetcode.com/problems/cat-and-mouse-ii/

object Solution {
  def canMouseWin(grid: Array[String], catJump: Int, mouseJump: Int): Boolean = {
    val rows = grid.length
    val cols = grid(0).length
    var totalOpen = 0
    var mouse = 0
    var cat = 0
    var food = 0
    for (r <- 0 until rows; c <- 0 until cols) {
      val cell = grid(r)(c)
      if (cell != '#') totalOpen += 1
      cell match {
        case 'M' => mouse = r * cols + c
        case 'C' => cat = r * cols + c
        case 'F' => food = r * cols + c
        case _ =>
      }
    }
    val dirs = Array((1, 0), (-1, 0), (0, 1), (0, -1))
    def computeMoves(pos: Int, jump: Int): Array[Int] = {
      val r = pos / cols
      val c = pos % cols
      val out = scala.collection.mutable.ArrayBuffer(pos)
      for ((dr, dc) <- dirs) {
        var step = 1
        var blocked = false
        while (step <= jump && !blocked) {
          val nr = r + dr * step
          val nc = c + dc * step
          if (nr < 0 || nr >= rows || nc < 0 || nc >= cols || grid(nr)(nc) == '#') {
            blocked = true
          } else {
            out += nr * cols + nc
            step += 1
          }
        }
      }
      out.toArray
    }
    val cells = rows * cols
    val mouseMoves = new Array[Array[Int]](cells)
    val catMoves = new Array[Array[Int]](cells)
    for (r <- 0 until rows; c <- 0 until cols) {
      if (grid(r)(c) != '#') {
        val pos = r * cols + c
        mouseMoves(pos) = computeMoves(pos, mouseJump)
        catMoves(pos) = computeMoves(pos, catJump)
      }
    }
    val maxTurn = 2 * totalOpen
    val memo = new Array[Byte](cells * cells * maxTurn)
    def win(m: Int, c: Int, turn: Int): Boolean = {
      if (turn >= maxTurn) return false
      if (m == food) return true
      if (c == food || c == m) return false
      val key = (m * cells + c) * maxTurn + turn
      if (memo(key) != 0) return memo(key) == 1
      val result =
        if (turn % 2 == 0) mouseMoves(m).exists(nm => win(nm, c, turn + 1))
        else catMoves(c).forall(nc => win(m, nc, turn + 1))
      memo(key) = if (result) 1 else 2
      result
    }
    win(mouse, cat, 0)
  }
}
