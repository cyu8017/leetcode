# LeetCode 3845 - Maximum Subarray XOR with Bounded Range
# https://leetcode.com/problems/maximum-subarray-xor-with-bounded-range/

# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def max_subarray_xor(nums, k)
  nodes = [{ next: [0, 0], count: 0 }]

  add = lambda do |x, delta|
    u = 0
    nodes[u][:count] += delta
    15.downto(0) do |b|
      bit = (x >> b) & 1
      if nodes[u][:next][bit] == 0
        nodes[u][:next][bit] = nodes.length
        nodes << { next: [0, 0], count: 0 }
      end
      u = nodes[u][:next][bit]
      nodes[u][:count] += delta
    end
  end

  query = lambda do |x|
    u = 0
    res = 0
    15.downto(0) do |b|
      bit = (x >> b) & 1
      want = bit ^ 1
      v = nodes[u][:next][want]
      if v != 0 && nodes[v][:count] > 0
        res |= 1 << b
        u = v
      else
        u = nodes[u][:next][bit]
      end
    end
    res
  end

  n = nums.length
  pref = Array.new(n + 1, 0)
  (0...n).each { |i| pref[i + 1] = pref[i] ^ nums[i] }
  max_q = []
  min_q = []
  left = 0
  trie_left = 0
  ans = 0
  (0...n).each do |r|
    x = nums[r]
    max_q.pop while !max_q.empty? && nums[max_q[-1]] <= x
    max_q << r
    min_q.pop while !min_q.empty? && nums[min_q[-1]] >= x
    min_q << r
    while nums[max_q[0]] - nums[min_q[0]] > k
      max_q.shift if max_q[0] == left
      min_q.shift if min_q[0] == left
      left += 1
    end
    add.call(pref[r], 1)
    while trie_left < left
      add.call(pref[trie_left], -1)
      trie_left += 1
    end
    cur = query.call(pref[r + 1])
    ans = cur if cur > ans
  end
  ans
end
