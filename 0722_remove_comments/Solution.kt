// LeetCode 0722 - Remove Comments
// https://leetcode.com/problems/remove-comments/

class Solution {
    fun removeComments(source: Array<String>): List<String> {
        val result = ArrayList<String>()
        val buffer = StringBuilder()
        var inBlock = false
        for (line in source) {
            var i = 0
            while (i < line.length) {
                if (inBlock) {
                    if (i + 1 < line.length && line[i] == '*' && line[i + 1] == '/') {
                        inBlock = false
                        i += 2
                    } else i++
                } else if (i + 1 < line.length && line[i] == '/' && line[i + 1] == '*') {
                    inBlock = true
                    i += 2
                } else if (i + 1 < line.length && line[i] == '/' && line[i + 1] == '/') break
                else buffer.append(line[i++])
            }
            if (!inBlock && buffer.isNotEmpty()) {
                result.add(buffer.toString())
                buffer.setLength(0)
            }
        }
        return result
    }
}
