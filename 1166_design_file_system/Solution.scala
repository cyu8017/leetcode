// LeetCode 1166 - Design File System
// https://leetcode.com/problems/design-file-system/

class FileSystem() {
  private val paths = scala.collection.mutable.Map("" -> -1)

  def createPath(path: String, value: Int): Boolean = {
    if (paths.contains(path)) return false
    val parent = path.substring(0, path.lastIndexOf('/'))
    if (!paths.contains(parent)) return false
    paths(path) = value
    true
  }

  def get(path: String): Int = paths.getOrElse(path, -1)
}
