# LeetCode 3711 - Maximum Transactions Without Negative Balance
# https://leetcode.com/problems/maximum-transactions-without-negative-balance/

# @param {Integer[]} transactions
# @return {Integer}
def max_transactions(transactions)
  tm = Hash.new(0)
  ans = transactions.length
  s = 0
  heap = []
  transactions.each do |x|
    s += x
    tm[x] += 1
    heap << x
    heap.sort!
    while s < 0
      heap.shift while !heap.empty? && tm[heap[0]] == 0
      y = heap[0]
      s -= y
      ans -= 1
      c = tm[y]
      if c == 1
        tm.delete(y)
        heap.shift
      else
        tm[y] = c - 1
        heap.shift
      end
    end
  end
  ans
end
