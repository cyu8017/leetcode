class Solution {
    fun titleToNumber(columnTitle: String): Int {
        var result = 0
        for (ch in columnTitle) {
            result = result * 26 + (ch - 'A' + 1)
        }
        return result
    }
}
