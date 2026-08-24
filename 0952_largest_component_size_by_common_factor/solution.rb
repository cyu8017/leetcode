# LeetCode 0952 - Largest Component Size by Common Factor
# https://leetcode.com/problems/largest-component-size-by-common-factor/

# @param {Integer[]} nums
# @return {Integer}
def largest_component_size(nums)
  parent = (0..nums.max).to_a

  find = lambda do |x|
    while parent[x] != x
      parent[x] = parent[parent[x]]
      x = parent[x]
    end
    x
  end

  union = ->(a, b) { parent[find.call(a)] = find.call(b) }

  factors = lambda do |x|
    res = []
    d = 2
    while d * d <= x
      if x % d == 0
        res << d
        x /= d while x % d == 0
      end
      d += 1
    end
    res << x if x > 1
    res
  end

  nums.each do |num|
    factors.call(num).each { |f| union.call(num, f) }
  end

  count = Hash.new(0)
  nums.each { |num| count[find.call(num)] += 1 }
  count.values.max
end
