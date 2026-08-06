// LeetCode 1233 - Remove Sub-Folders from the Filesystem
// https://leetcode.com/problems/remove-sub-folders-from-the-filesystem/

object Solution {
  def removeSubfolders(folder: Array[String]): List[String] = {
    val answer = scala.collection.mutable.ListBuffer.empty[String]
    for (path <- folder.sorted) {
      if (answer.isEmpty || !path.startsWith(answer.last + "/")) answer += path
    }
    answer.toList
  }
}
