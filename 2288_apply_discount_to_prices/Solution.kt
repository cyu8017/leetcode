// LeetCode 2288 - Apply Discount to Prices
// https://leetcode.com/problems/apply-discount-to-prices/

class Solution {
    fun discountPrices(sentence: String, discount: Int): String {
        val parts = sentence.split(" ").toTypedArray()
        for (i in parts.indices) {
            val part = parts[i]
            if (part.length >= 2 && part[0] == '$') {
                var ok = true
                for (j in 1 until part.length) {
                    if (part[j] < '0' || part[j] > '9') {
                        ok = false
                        break
                    }
                }
                if (ok) {
                    val v = part.substring(1).toLong()
                    val price = v * (100.0 - discount) / 100.0
                    parts[i] = String.format("$%.2f", price)
                }
            }
        }
        return parts.joinToString(" ")
    }
}
