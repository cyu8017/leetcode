
MOD = 10**9 + 7

# @param {Integer[][]} orders
# @return {Integer}
def get_number_of_backlog_orders(orders)
  buy = []
  sell = []

  orders.each do |price, amount, order_type|
    if order_type == 0
      heap_push(buy, [-price, amount])
    else
      heap_push(sell, [price, amount])
    end

    while !buy.empty? && !sell.empty? && -buy[0][0] >= sell[0][0]
      buy_price = -buy[0][0]
      buy_amount = buy[0][1]
      sell_price = sell[0][0]
      sell_amount = sell[0][1]
      matched = [buy_amount, sell_amount].min
      buy_amount -= matched
      sell_amount -= matched
      heap_pop(buy)
      heap_pop(sell)
      heap_push(buy, [-buy_price, buy_amount]) if buy_amount > 0
      heap_push(sell, [sell_price, sell_amount]) if sell_amount > 0
    end
  end

  total = 0
  buy.each { |_, amount| total = (total + amount) % MOD }
  sell.each { |_, amount| total = (total + amount) % MOD }
  total
end

def heap_push(heap, item)
  heap << item
  i = heap.length - 1
  while i > 0
    p = (i - 1) / 2
    break if heap[p][0] < heap[i][0] || (heap[p][0] == heap[i][0] && heap[p][1] <= heap[i][1])
    heap[p], heap[i] = heap[i], heap[p]
    i = p
  end
end

def heap_pop(heap)
  top = heap[0]
  last = heap.pop
  return top if heap.empty?
  heap[0] = last
  i = 0
  n = heap.length
  loop do
    l = 2 * i + 1
    r = 2 * i + 2
    smallest = i
    if l < n && (heap[l][0] < heap[smallest][0] || (heap[l][0] == heap[smallest][0] && heap[l][1] < heap[smallest][1]))
      smallest = l
    end
    if r < n && (heap[r][0] < heap[smallest][0] || (heap[r][0] == heap[smallest][0] && heap[r][1] < heap[smallest][1]))
      smallest = r
    end
    break if smallest == i
    heap[smallest], heap[i] = heap[i], heap[smallest]
    i = smallest
  end
  top
end
