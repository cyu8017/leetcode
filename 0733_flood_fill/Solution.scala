// LeetCode 0733 - Flood Fill
// https://leetcode.com/problems/flood-fill/

object Solution {
  def floodFill(image: Array[Array[Int]], sr: Int, sc: Int, color: Int): Array[Array[Int]] = {
    val original = image(sr)(sc)
    if (original == color) return image
    def dfs(r: Int, c: Int): Unit = {
      if (r < 0 || r >= image.length || c < 0 || c >= image(0).length || image(r)(c) != original) return
      image(r)(c) = color
      dfs(r + 1, c)
      dfs(r - 1, c)
      dfs(r, c + 1)
      dfs(r, c - 1)
    }
    dfs(sr, sc)
    image
  }
}
