// LeetCode 3822 - Design Order Management System
// https://leetcode.com/problems/design_order_management_system/

class OrderManagementSystem() {
  private case class Key(orderType: String, price: Int)
  private val orderTypeMap = scala.collection.mutable.Map.empty[Int, String]
  private val priceMap = scala.collection.mutable.Map.empty[Int, Int]
  private val t = scala.collection.mutable.Map.empty[Key, scala.collection.mutable.ArrayBuffer[Int]]

  def addOrder(orderId: Int, orderType: String, price: Int): Unit = {
    orderTypeMap(orderId) = orderType
    priceMap(orderId) = price
    val key = Key(orderType, price)
    t.getOrElseUpdate(key, scala.collection.mutable.ArrayBuffer.empty[Int]) += orderId
  }

  def modifyOrder(orderId: Int, newPrice: Int): Unit = {
    val orderType = orderTypeMap(orderId)
    val oldPrice = priceMap(orderId)
    priceMap(orderId) = newPrice
    val oldList = t(Key(orderType, oldPrice))
    var i = 0
    while (i < oldList.length) {
      if (oldList(i) == orderId) {
        oldList.remove(i)
        i = oldList.length
      } else i += 1
    }
    t.getOrElseUpdate(Key(orderType, newPrice), scala.collection.mutable.ArrayBuffer.empty[Int]) += orderId
  }

  def cancelOrder(orderId: Int): Unit = {
    val orderType = orderTypeMap(orderId)
    val price = priceMap(orderId)
    orderTypeMap.remove(orderId)
    priceMap.remove(orderId)
    val list = t(Key(orderType, price))
    var i = 0
    while (i < list.length) {
      if (list(i) == orderId) {
        list.remove(i)
        i = list.length
      } else i += 1
    }
  }

  def getOrdersAtPrice(orderType: String, price: Int): Array[Int] = {
    t.get(Key(orderType, price)) match {
      case None => Array.emptyIntArray
      case Some(list) => list.toArray
    }
  }
}
