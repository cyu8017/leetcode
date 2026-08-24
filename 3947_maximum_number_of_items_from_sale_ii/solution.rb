# LeetCode 3947 - Maximum Number of Items From Sale II
# https://leetcode.com/problems/maximum-number-of-items-from-sale-ii/

# @param {Integer[][]} items
# @param {Integer} budget
# @return {Integer}
def max_items(items, budget)
  n = items.length
  frequency = Array.new(n + 1, 0)
  minimum_price = items[0][1]
  items.each do |item|
    frequency[item[0]] += 1
    minimum_price = item[1] if item[1] < minimum_price
  end
  batches = []
  items.each do |item|
    gain = 0
    multiple = item[0]
    while multiple <= n
      gain += frequency[multiple]
      multiple += item[0]
    end
    gain -= 1
    batches << [item[1], gain] if gain > 0 && item[1] < 2 * minimum_price
  end
  batches.sort_by! { |a| a[0] }
  remaining = budget
  answer = budget / minimum_price
  boosted = 0
  batches.each do |current|
    count = current[1]
    affordable = remaining / current[0]
    count = affordable if affordable < count
    remaining -= count * current[0]
    boosted += count
    total = 2 * boosted + remaining / minimum_price
    answer = total if total > answer
    break if count < current[1]
  end
  answer
end
