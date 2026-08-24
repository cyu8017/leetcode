# LeetCode 2709 - Greatest Common Divisor Traversal
# https://leetcode.com/problems/greatest-common-divisor-traversal/

# @param {Integer[]} nums
# @return {Boolean}
def can_traverse_all_pairs(nums)
  n = nums.length
  return true if n == 1

  mx = nums[0]
  nums.each { |x| mx = x if x > mx }
  parent = (0..mx).to_a
  find = nil
  find = lambda do |x|
    parent[x] = find.call(parent[x]) if parent[x] != x
    parent[x]
  end
  unite = lambda do |a, b|
    ra = find.call(a)
    rb = find.call(b)
    parent[ra] = rb if ra != rb
  end
  has = Array.new(mx + 1, false)
  nums.each do |x|
    return false if x == 1

    has[x] = true
  end
  sieve = Array.new(mx + 1, 0)
  (2..mx).each do |i|
    next unless sieve[i] == 0

    i.step(mx, i) do |j|
      sieve[j] = i if sieve[j] == 0
      unite.call(i, j) if has[j]
    end
  end
  root = find.call(nums[0])
  nums.each { |x| return false if find.call(x) != root }
  true
end
