# LeetCode 0599 - Minimum Index Sum of Two Lists
# https://leetcode.com/problems/minimum-index-sum-of-two-lists/

# @param {String[]} list1
# @param {String[]} list2
# @return {String[]}
def find_restaurant(list1, list2)
  index1 = {}
  list1.each_with_index { |name, i| index1[name] = i }
  best = Float::INFINITY
  answer = []

  list2.each_with_index do |name, j|
    next unless index1.key?(name)

    total = index1[name] + j
    if total < best
      best = total
      answer = [name]
    elsif total == best
      answer << name
    end
  end

  answer
end
