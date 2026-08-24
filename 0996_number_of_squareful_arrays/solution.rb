# LeetCode 0996 - Number of Squareful Arrays
# https://leetcode.com/problems/number-of-squareful-arrays/

# @param {Integer[]} nums
# @return {Integer}
def num_squareful_perms(nums)
  count = Hash.new(0)
  nums.each { |x| count[x] += 1 }
  graph = {}
  count.each_key { |x| graph[x] = [] }
  count.each_key do |a|
    count.each_key do |b|
      s = a + b
      r = Integer.sqrt(s)
      graph[a] << b if r * r == s
    end
  end
  ans = 0
  dfs = lambda do |x, remain|
    if remain.zero?
      ans += 1
      return
    end
    graph[x].each do |y|
      next unless count[y].positive?

      count[y] -= 1
      dfs.call(y, remain - 1)
      count[y] += 1
    end
  end
  count.each_key do |x|
    count[x] -= 1
    dfs.call(x, nums.length - 1)
    count[x] += 1
  end
  ans
end
