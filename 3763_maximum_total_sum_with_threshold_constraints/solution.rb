# LeetCode 3763 - Maximum Total Sum with Threshold Constraints
# https://leetcode.com/problems/maximum-total-sum-with-threshold-constraints/

# @param {Integer[]} nums
# @param {Integer[]} threshold
# @return {Integer}
def max_sum(nums, threshold)
  n = nums.length
  idx = (0...n).to_a.sort_by { |i| threshold[i] }
  tree = []
  push = lambda do |x|
    tree << x
    i = tree.length - 1
    while i > 0
      p = (i - 1) >> 1
      break if tree[i] <= tree[p]
      tree[i], tree[p] = tree[p], tree[i]
      i = p
    end
  end
  pop = lambda do
    top = tree[0]
    last = tree.pop
    if !tree.empty?
      tree[0] = last
      i = 0
      loop do
        s = i
        l = i * 2 + 1
        r = l + 1
        s = l if l < tree.length && tree[l] > tree[s]
        s = r if r < tree.length && tree[r] > tree[s]
        break if s == i
        tree[i], tree[s] = tree[s], tree[i]
        i = s
      end
    end
    top
  end
  ans = 0
  i = 0
  step = 1
  loop do
    while i < n && threshold[idx[i]] <= step
      push.call(nums[idx[i]])
      i += 1
    end
    break if tree.empty?
    ans += pop.call
    step += 1
  end
  ans
end
