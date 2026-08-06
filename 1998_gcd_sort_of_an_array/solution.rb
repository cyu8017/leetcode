# LeetCode 1998 - GCD Sort of an Array
# https://leetcode.com/problems/gcd-sort-of-an-array/

# @param {Integer[]} nums
# @return {Boolean}
def gcd_sort(nums)
  m = nums.max
  parent = (0..m).to_a

  find = lambda do |x|
    while parent[x] != x
      parent[x] = parent[parent[x]]
      x = parent[x]
    end
    x
  end

  union = lambda do |a, b|
    ra = find.call(a)
    rb = find.call(b)
    parent[rb] = ra if ra != rb
  end

  spf = (0..m).to_a
  (2..(m**0.5).to_i).each do |i|
    next unless spf[i] == i
    (i * i).step(m, i) do |j|
      spf[j] = i if spf[j] == j
    end
  end

  nums.uniq.each do |x|
    y = x
    while y > 1
      p = spf[y]
      union.call(x, p)
      y /= p while (y % p).zero?
    end
  end

  sorted_nums = nums.sort
  nums.zip(sorted_nums).all? { |a, b| find.call(a) == find.call(b) }
end
