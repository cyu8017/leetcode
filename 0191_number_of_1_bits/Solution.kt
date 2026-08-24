class Solution {
    fun hammingWeight(n: Int): Int {
        var value = n
        var count = 0
        while (value != 0) {
            value = value and (value - 1)
            count++
        }
        return count
    }
}
