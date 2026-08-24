// LeetCode 2166 - Design Bitset
// https://leetcode.com/problems/design-bitset/

class Bitset(private val size: Int) {
    private val bits = CharArray(size)
    private var ones = 0
    private var flipped = false

    fun fix(idx: Int) {
        val target = if (flipped) 0.toChar() else 1.toChar()
        if (bits[idx] != target) {
            bits[idx] = target
            ones += if (flipped) -1 else 1
        }
    }

    fun unfix(idx: Int) {
        val target = if (flipped) 1.toChar() else 0.toChar()
        if (bits[idx] != target) {
            bits[idx] = target
            ones += if (flipped) 1 else -1
        }
    }

    fun flip() {
        flipped = !flipped
        ones = size - ones
    }

    fun all(): Boolean = ones == size
    fun one(): Boolean = ones > 0
    fun count(): Int = ones

    override fun toString(): String {
        val b = CharArray(size)
        for (i in 0 until size) {
            var v = bits[i]
            if (flipped) v = (v.code xor 1).toChar()
            b[i] = ('0'.code + v.code).toChar()
        }
        return String(b)
    }
}
