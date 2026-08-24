// LeetCode 0900 - RLE Iterator
// https://leetcode.com/problems/rle-iterator/

class RLEIterator(encoding: IntArray) {
    private val enc = encoding.copyOf()
    private var i = 0

    fun next(n: Int): Int {
        var n = n
        while (i < enc.size) {
            if (enc[i] >= n) {
                enc[i] -= n
                return enc[i + 1]
            }
            n -= enc[i]
            i += 2
        }
        return -1
    }
}
