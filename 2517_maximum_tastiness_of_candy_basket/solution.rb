# LeetCode 2517 - Maximum Tastiness of Candy Basket
# https://leetcode.com/problems/maximum-tastiness-of-candy-basket/

# @param {Integer[]} price
# @param {Integer} k
# @return {Integer}
def maximum_tastiness(price, k)
  price = price.sort
  ok = lambda do |d|
    cnt = 1
    last = price[0]
    (1...price.length).each do |i|
      if price[i] - last >= d
        cnt += 1
        last = price[i]
        return true if cnt >= k
      end
    end
    false
  end

  lo = 0
  hi = price[-1] - price[0]
  while lo < hi
    mid = (lo + hi + 1) / 2
    if ok.call(mid)
      lo = mid
    else
      hi = mid - 1
    end
  end
  lo
end
