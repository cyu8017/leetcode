# LeetCode 2548 - Maximum Price to Fill a Bag
# https://leetcode.com/problems/maximum-price-to-fill-a-bag/

# @param {Integer[][]} items
# @param {Integer} capacity
# @return {Float}
def max_price(items, capacity)
  items = items.sort_by { |it| -(it[0].to_f / it[1]) }
  ans = 0.0
  remain = capacity
  items.each do |price, weight|
    if remain >= weight
      ans += price
      remain -= weight
    else
      ans += price.to_f * remain / weight
      remain = 0
      break
    end
  end
  return -1 if remain > 0

  ans
end

alias solve max_price
