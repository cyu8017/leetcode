// LeetCode 0588 - Design In-Memory File System
// https://leetcode.com/problems/design-in-memory-file-system/

import scala.collection.mutable

class FileSystem() {
  private class Node {
    var isFile = false
    var content = ""
    val children = mutable.TreeMap.empty[String, Node]
  }

  private val root = new Node()

  def ls(path: String): List[String] = {
    if (path == "/") return root.children.keys.toList
    val parts = split(path)
    var node = root
    parts.foreach(part => node = node.children(part))
    if (node.isFile) List(parts.last)
    else node.children.keys.toList
  }

  def mkdir(path: String): Unit = {
    var node = root
    split(path).foreach { part =>
      if (!node.children.contains(part)) node.children(part) = new Node()
      node = node.children(part)
    }
  }

  def addContentToFile(filePath: String, content: String): Unit = {
    val parts = split(filePath)
    var node = root
    var i = 0
    while (i + 1 < parts.size) {
      if (!node.children.contains(parts(i))) node.children(parts(i)) = new Node()
      node = node.children(parts(i))
      i += 1
    }
    val name = parts.last
    if (!node.children.contains(name)) node.children(name) = new Node()
    val file = node.children(name)
    file.isFile = true
    file.content += content
  }

  def readContentFromFile(filePath: String): String = {
    var node = root
    split(filePath).foreach(part => node = node.children(part))
    node.content
  }

  private def split(path: String): List[String] =
    path.split("/").filter(_.nonEmpty).toList
}
