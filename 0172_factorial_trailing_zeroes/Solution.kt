class Solution {
    fun trailingZeroes(n: Int): Int {
        var value = n
        var count = 0
        while (value > 0) {
            value /= 5
            count += value
        }
        return count
    }
}
