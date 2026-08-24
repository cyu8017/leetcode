// LeetCode 2034 - Stock Price Fluctuation
// https://leetcode.com/problems/stock-price-fluctuation/

class StockPrice {
    private var latestTs = 0
    private val priceAt = HashMap<Int, Int>()
    private val maxHeap = java.util.PriorityQueue<IntArray> { a, b -> b[0].compareTo(a[0]) }
    private val minHeap = java.util.PriorityQueue<IntArray> { a, b -> a[0].compareTo(b[0]) }

    fun update(timestamp: Int, price: Int) {
        priceAt[timestamp] = price
        if (timestamp >= latestTs) latestTs = timestamp
        maxHeap.add(intArrayOf(price, timestamp))
        minHeap.add(intArrayOf(price, timestamp))
    }

    fun current(): Int = priceAt[latestTs]!!

    fun maximum(): Int {
        while (true) {
            val top = maxHeap.peek()
            if (priceAt[top[1]] == top[0]) return top[0]
            maxHeap.poll()
        }
    }

    fun minimum(): Int {
        while (true) {
            val top = minHeap.peek()
            if (priceAt[top[1]] == top[0]) return top[0]
            minHeap.poll()
        }
    }
}
