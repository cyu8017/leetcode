# LeetCode 3943 - Number of Pairs After Increment
# https://leetcode.com/problems/number-of-pairs-after-increment/

# @param {Integer[]} nums1
# @param {Integer[]} nums2
# @param {Integer[][]} queries
# @return {Integer[]}
def number_of_pairs(nums1, nums2, queries)
  rebuild = lambda do |freq, nums2, b, block_size, n|
    freq[b] = {}
    finish = [(b + 1) * block_size, n].min
    (b * block_size...finish).each do |i|
      freq[b][nums2[i]] = freq[b].fetch(nums2[i], 0) + 1
    end
  end
  push = lambda do |lazy, nums2, b, block_size, n|
    if lazy[b] != 0
      finish = [(b + 1) * block_size, n].min
      (b * block_size...finish).each { |i| nums2[i] += lazy[b] }
      lazy[b] = 0
    end
  end
  block_size = 225
  n = nums2.length
  blocks = (n + block_size - 1) / block_size
  lazy = Array.new(blocks, 0)
  freq = Array.new(blocks) { {} }
  blocks.times { |b| rebuild.call(freq, nums2, b, block_size, n) }
  fixed = {}
  nums1.each { |x| fixed[x] = fixed.fetch(x, 0) + 1 }
  answer = []
  queries.each do |q|
    if q[0] == 1
      l, r, delta = q[1], q[2], q[3]
      first = l / block_size
      last = r / block_size
      if first == last
        push.call(lazy, nums2, first, block_size, n)
        (l..r).each { |i| nums2[i] += delta }
        rebuild.call(freq, nums2, first, block_size, n)
        next
      end
      push.call(lazy, nums2, first, block_size, n)
      (l...((first + 1) * block_size)).each { |i| nums2[i] += delta }
      rebuild.call(freq, nums2, first, block_size, n)
      push.call(lazy, nums2, last, block_size, n)
      ((last * block_size)..r).each { |i| nums2[i] += delta }
      rebuild.call(freq, nums2, last, block_size, n)
      ((first + 1)...last).each { |b| lazy[b] += delta }
    else
      total = 0
      fixed.each do |a, count_a|
        target = q[1] - a
        blocks.times do |b|
          c = freq[b][target - lazy[b]]
          total += count_a * c if c
        end
      end
      answer << total
    end
  end
  answer
end
