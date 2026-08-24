// LeetCode 2424 - Longest Uploaded Prefix
// https://leetcode.com/problems/longest-uploaded-prefix/

class LUPrefix(_n: Int) {
  private val uploaded = new Array[Boolean](_n + 2)
  private var prefixLen = 0

  def upload(video: Int): Unit = {
    uploaded(video) = true
    while (uploaded(prefixLen + 1)) prefixLen += 1
  }

  def longest(): Int = prefixLen
}
