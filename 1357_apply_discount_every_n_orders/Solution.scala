class Cashier(n: Int, discount: Int, products: Array[Int], prices: Array[Int]) {
  private val price = products.zip(prices).toMap
  private var count = 0
  def getBill(product: Array[Int], amount: Array[Int]): Double = {
    count += 1
    val total = product.indices.map(i => price(product(i)).toDouble * amount(i)).sum
    if (count % n == 0) total * (100 - discount) / 100.0 else total
  }
}
