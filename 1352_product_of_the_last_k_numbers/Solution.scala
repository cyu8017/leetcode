import scala.collection.mutable

class ProductOfNumbers {
  private val prefix = mutable.ArrayBuffer(1)
  def add(num: Int): Unit = if (num == 0) { prefix.clear(); prefix += 1 } else prefix += prefix.last * num
  def getProduct(k: Int): Int = if (k >= prefix.length) 0 else prefix.last / prefix(prefix.length - 1 - k)
}
