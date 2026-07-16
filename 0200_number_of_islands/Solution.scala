object Solution {
  def numIslands(grid: Array[Array[Char]]): Int = {
    if (grid.isEmpty) return 0
    def dfs(row: Int, col: Int): Unit = {
      if (row < 0 || row >= grid.length || col < 0 || col >= grid(0).length || grid(row)(col) != '1') return
      grid(row)(col) = '0'
      dfs(row + 1, col)
      dfs(row - 1, col)
      dfs(row, col + 1)
      dfs(row, col - 1)
    }
    var count = 0
    for (row <- grid.indices; col <- grid(0).indices) {
      if (grid(row)(col) == '1') {
        count += 1
        dfs(row, col)
      }
    }
    count
  }
}
