// LeetCode 1352 - Product of the Last K Numbers
// https://leetcode.com/problems/product-of-the-last-k-numbers/

class ProductOfNumbers {
    private val prefix = mutableListOf(1)

    fun add(num: Int) {
        if (num == 0) {
            prefix.clear()
            prefix.add(1)
        } else {
            prefix.add(prefix.last() * num)
        }
    }

    fun getProduct(k: Int): Int {
        return if (k >= prefix.size) 0 else prefix.last() / prefix[prefix.size - 1 - k]
    }
}
