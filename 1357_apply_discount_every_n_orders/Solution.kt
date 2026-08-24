// LeetCode 1357 - Apply Discount Every n Orders
// https://leetcode.com/problems/apply-discount-every-n-orders/

class Cashier(private val n: Int, private val discount: Int, products: IntArray, prices: IntArray) {
    private val price = HashMap<Int, Int>()
    private var count = 0

    init {
        for (i in products.indices) {
            price[products[i]] = prices[i]
        }
    }

    fun getBill(product: IntArray, amount: IntArray): Double {
        count++
        var total = 0.0
        for (i in product.indices) {
            total += price[product[i]]!! * amount[i]
        }
        return if (count % n == 0) total * (100 - discount) / 100.0 else total
    }
}
