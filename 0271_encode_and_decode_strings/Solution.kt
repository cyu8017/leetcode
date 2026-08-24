// LeetCode 0271 - Encode and Decode Strings
// https://leetcode.com/problems/encode-and-decode-strings/

class Codec {
    fun encode(strs: List<String>): String {
        return strs.joinToString("") { "${it.length}#$it" }
    }

    fun decode(encoded: String): List<String> {
        val result = mutableListOf<String>()
        var index = 0
        while (index < encoded.length) {
            val delimiter = encoded.indexOf('#', index)
            val length = encoded.substring(index, delimiter).toInt()
            val start = delimiter + 1
            result.add(encoded.substring(start, start + length))
            index = start + length
        }
        return result
    }
}
