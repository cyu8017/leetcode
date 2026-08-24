// LeetCode 2424 - Longest Uploaded Prefix
// https://leetcode.com/problems/longest-uploaded-prefix/

class LUPrefix(n: Int) {
    private val uploaded = BooleanArray(n + 2)
    private var prefixLen = 0

    fun upload(video: Int) {
        uploaded[video] = true
        while (uploaded[prefixLen + 1]) prefixLen++
    }

    fun longest(): Int = prefixLen
}
