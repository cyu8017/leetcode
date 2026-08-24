# LeetCode 3901 - Good Subsequence Queries
# https://leetcode.com/problems/good-subsequence-queries/

def gcd3901(a, b)
  while b != 0
    a, b = b, a % b
  end
  a
end

class SegmentTree3901
  attr_reader :tr

  def initialize(n)
    @tr = Array.new(n << 2) { { l: 0, r: 0, g: 0 } }
    build(1, 1, n)
  end

  def build(u, l, r)
    @tr[u][:l] = l
    @tr[u][:r] = r
    @tr[u][:g] = 0
    return if l == r
    mid = (l + r) >> 1
    build(u << 1, l, mid)
    build(u << 1 | 1, mid + 1, r)
  end

  def pushup(u)
    @tr[u][:g] = gcd3901(@tr[u << 1][:g], @tr[u << 1 | 1][:g])
  end

  def modify(u, x, v)
    if @tr[u][:l] == @tr[u][:r]
      @tr[u][:g] = v
      return
    end
    mid = (@tr[u][:l] + @tr[u][:r]) >> 1
    if x <= mid
      modify(u << 1, x, v)
    else
      modify(u << 1 | 1, x, v)
    end
    pushup(u)
  end

  def query(u, l, r)
    return 0 if l > r
    return @tr[u][:g] if @tr[u][:l] >= l && @tr[u][:r] <= r
    mid = (@tr[u][:l] + @tr[u][:r]) >> 1
    return query(u << 1, l, r) if r <= mid
    return query(u << 1 | 1, l, r) if l > mid
    gcd3901(query(u << 1, l, mid), query(u << 1 | 1, mid + 1, r))
  end
end

# @param {Integer[]} nums
# @param {Integer} p
# @param {Integer[][]} queries
# @return {Integer}
def count_good_subseq(nums, p, queries)
  n = nums.length
  tree = SegmentTree3901.new(n)
  cnt = 0
  n.times do |i|
    if nums[i] % p == 0
      tree.modify(1, i + 1, nums[i])
      cnt += 1
    end
  end
  ans = 0
  queries.each do |q|
    idx, val = q[0], q[1]
    if nums[idx] % p == 0
      tree.modify(1, idx + 1, 0)
      cnt -= 1
    end
    if val % p == 0
      tree.modify(1, idx + 1, val)
      cnt += 1
    end
    nums[idx] = val
    next if tree.tr[1][:g] != p
    if cnt < n || n > 6
      ans += 1
      next
    end
    (1..n).each do |i|
      left_g = tree.query(1, 1, i - 1)
      right_g = tree.query(1, i + 1, n)
      if gcd3901(left_g, right_g) == p
        ans += 1
        break
      end
    end
  end
  ans
end
