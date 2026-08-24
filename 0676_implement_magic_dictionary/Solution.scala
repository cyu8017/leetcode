// LeetCode 0676 - Implement Magic Dictionary
// https://leetcode.com/problems/implement-magic-dictionary/

class MagicDictionary() {
  private var words: Array[String] = Array.empty

  def buildDict(dictionary: Array[String]): Unit = {
    words = dictionary
  }

  def search(searchWord: String): Boolean = {
    words.exists { word =>
      if (word.length != searchWord.length) false
      else {
        var diff = 0
        var i = 0
        while (i < word.length) {
          if (word.charAt(i) != searchWord.charAt(i)) diff += 1
          i += 1
        }
        diff == 1
      }
    }
  }
}
