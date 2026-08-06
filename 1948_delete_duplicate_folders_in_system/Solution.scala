// LeetCode 1948 - Delete Duplicate Folders in System
// https://leetcode.com/problems/delete-duplicate-folders-in-system/

object Solution {
  private class Node {
    val children = scala.collection.mutable.TreeMap.empty[String, Node]
  }

  def deleteDuplicateFolder(paths: Array[List[String]]): List[List[String]] = {
    val root = new Node
    for (path <- paths) {
      var node = root
      for (folder <- path) {
        node = node.children.getOrElseUpdate(folder, new Node)
      }
    }

    val dup = scala.collection.mutable.Map.empty[String, Boolean]
    val serialOf = scala.collection.mutable.Map.empty[Int, String]

    def serialize(node: Node): String = {
      if (node.children.isEmpty) return ""
      val parts = node.children.toSeq.map { case (name, child) =>
        name + "(" + serialize(child) + ")"
      }
      val serial = parts.mkString
      if (serial.nonEmpty) {
        if (dup.contains(serial)) dup(serial) = true
        else dup(serial) = false
        serialOf(System.identityHashCode(node)) = serial
      }
      serial
    }

    serialize(root)

    val ans = scala.collection.mutable.ListBuffer.empty[List[String]]
    def collect(node: Node, path: scala.collection.mutable.ListBuffer[String]): Unit = {
      for ((name, child) <- node.children) {
        val serial = serialOf.getOrElse(System.identityHashCode(child), "")
        if (serial.nonEmpty && dup.getOrElse(serial, false)) ()
        else {
          path += name
          ans += path.toList
          collect(child, path)
          path.remove(path.length - 1)
        }
      }
    }
    collect(root, scala.collection.mutable.ListBuffer.empty[String])
    ans.toList
  }
}
