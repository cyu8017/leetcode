// LeetCode 3822 - Design Order Management System
// https://leetcode.com/problems/design-order-management-system/

class OrderManagementSystem {
    private data class Key(val orderType: String, val price: Int)

    private val orderTypeMap = HashMap<Int, String>()
    private val priceMap = HashMap<Int, Int>()
    private val t = HashMap<Key, ArrayList<Int>>()

    fun addOrder(orderId: Int, orderType: String, price: Int) {
        orderTypeMap[orderId] = orderType
        priceMap[orderId] = price
        val key = Key(orderType, price)
        t.getOrPut(key) { ArrayList() }.add(orderId)
    }

    fun modifyOrder(orderId: Int, newPrice: Int) {
        val orderType = orderTypeMap[orderId]!!
        val oldPrice = priceMap[orderId]!!
        priceMap[orderId] = newPrice
        val oldKey = Key(orderType, oldPrice)
        val oldList = t[oldKey]!!
        for (i in oldList.indices) {
            if (oldList[i] == orderId) {
                oldList.removeAt(i)
                break
            }
        }
        val key = Key(orderType, newPrice)
        t.getOrPut(key) { ArrayList() }.add(orderId)
    }

    fun cancelOrder(orderId: Int) {
        val orderType = orderTypeMap[orderId]!!
        val price = priceMap[orderId]!!
        orderTypeMap.remove(orderId)
        priceMap.remove(orderId)
        val key = Key(orderType, price)
        val list = t[key]!!
        for (i in list.indices) {
            if (list[i] == orderId) {
                list.removeAt(i)
                break
            }
        }
    }

    fun getOrdersAtPrice(orderType: String, price: Int): IntArray {
        val key = Key(orderType, price)
        val list = t[key] ?: return IntArray(0)
        val ans = IntArray(list.size)
        for (i in list.indices) ans[i] = list[i]
        return ans
    }
}
