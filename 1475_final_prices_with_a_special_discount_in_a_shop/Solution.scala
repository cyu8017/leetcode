object Solution {
  def finalPrices(prices: Array[Int]): Array[Int] = {
    val answer = prices.clone()
    val stack = scala.collection.mutable.Stack.empty[Int]
    for (i <- prices.indices) {
      while (stack.nonEmpty && prices(stack.top) >= prices(i)) answer(stack.pop()) -= prices(i)
      stack.push(i)
    }
    answer
  }
}
