// LeetCode 2296 - Design a Text Editor
// https://leetcode.com/problems/design-a-text-editor/

class TextEditor() {
  private val left = scala.collection.mutable.ArrayBuffer.empty[Char]
  private val right = scala.collection.mutable.ArrayBuffer.empty[Char]

  private def suffix(): String = {
    val start = math.max(0, left.length - 10)
    val sb = new StringBuilder
    var i = start
    while (i < left.length) {
      sb.append(left(i))
      i += 1
    }
    sb.toString
  }

  def addText(text: String): Unit = {
    var i = 0
    while (i < text.length) {
      left += text.charAt(i)
      i += 1
    }
  }

  def deleteText(k0: Int): Int = {
    var k = k0
    var deleted = 0
    while (k > 0 && left.nonEmpty) {
      left.remove(left.length - 1)
      k -= 1
      deleted += 1
    }
    deleted
  }

  def cursorLeft(k0: Int): String = {
    var k = k0
    while (k > 0 && left.nonEmpty) {
      right += left.remove(left.length - 1)
      k -= 1
    }
    suffix()
  }

  def cursorRight(k0: Int): String = {
    var k = k0
    while (k > 0 && right.nonEmpty) {
      left += right.remove(right.length - 1)
      k -= 1
    }
    suffix()
  }
}
