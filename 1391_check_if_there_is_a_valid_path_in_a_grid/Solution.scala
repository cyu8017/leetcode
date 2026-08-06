object Solution {
  def hasValidPath(grid: Array[Array[Int]]): Boolean = {
    val dirs = Array[Array[(Int, Int)]](
      Array.empty,
      Array((0, -1), (0, 1)),
      Array((-1, 0), (1, 0)),
      Array((0, -1), (1, 0)),
      Array((0, 1), (1, 0)),
      Array((0, -1), (-1, 0)),
      Array((0, 1), (-1, 0))
    )
    val m = grid.length; val n = grid(0).length; val seen = scala.collection.mutable.Set((0,0)); val q = scala.collection.mutable.Stack((0,0))
    while (q.nonEmpty) { val (r,c) = q.pop(); if (r == m-1 && c == n-1) return true; dirs(grid(r)(c)).foreach { case (dr,dc) => val x=r+dr; val y=c+dc; if (x>=0 && x<m && y>=0 && y<n && !seen((x,y)) && dirs(grid(x)(y)).contains((-dr,-dc))) { seen += ((x,y)); q.push((x,y)) } } }; false
  }
}
