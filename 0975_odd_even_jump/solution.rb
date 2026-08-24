# LeetCode 0975 - Odd Even Jump
# https://leetcode.com/problems/odd-even-jump/

# @param {Integer[]} arr
# @return {Integer}
def odd_even_jumps(arr)
  n = arr.length
  next_higher = Array.new(n, 0)
  next_lower = Array.new(n, 0)
  stack = []
  arr.each_with_index.sort_by { |a, i| [a, i] }.each do |_a, i|
    while !stack.empty? && stack[-1] < i
      next_higher[stack.pop] = i
    end
    stack << i
  end
  stack.clear
  arr.each_with_index.sort_by { |a, i| [-a, i] }.each do |_a, i|
    while !stack.empty? && stack[-1] < i
      next_lower[stack.pop] = i
    end
    stack << i
  end

  odd = Array.new(n, false)
  even = Array.new(n, false)
  odd[-1] = even[-1] = true
  (n - 2).downto(0) do |i|
    odd[i] = even[next_higher[i]] if next_higher[i] != 0
    even[i] = odd[next_lower[i]] if next_lower[i] != 0
  end
  odd.count(true)
end
