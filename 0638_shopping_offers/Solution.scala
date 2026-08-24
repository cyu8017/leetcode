// LeetCode 0638 - Shopping Offers
// https://leetcode.com/problems/shopping-offers/

import scala.collection.mutable

object Solution {
  def shoppingOffers(price: List[Int], special: List[List[Int]], needs: List[Int]): Int = {
    val memo = mutable.Map.empty[List[Int], Int]
    def dfs(state: List[Int]): Int = {
      memo.get(state) match {
        case Some(cached) => cached
        case None =>
          var cost = 0
          var i = 0
          while (i < price.size) {
            cost += state(i) * price(i)
            i += 1
          }
          special.foreach { offer =>
            val nxt = state.toArray
            var valid = true
            i = 0
            while (i < price.size && valid) {
              if (nxt(i) < offer(i)) valid = false
              else nxt(i) -= offer(i)
              i += 1
            }
            if (valid) cost = math.min(cost, offer(price.size) + dfs(nxt.toList))
          }
          memo(state) = cost
          cost
      }
    }
    dfs(needs)
  }
}
