# LeetCode 3049 - Earliest Second to Mark Indices II
# https://leetcode.com/problems/earliest-second-to-mark-indices-ii/

# @param {Integer[]} nums
# @param {Integer[]} change_indices
# @return {Integer}
def earliest_second_to_mark_indices(nums, change_indices)
  second_to_index = get_second_to_index(nums, change_indices)
  nums_sum = nums.sum
  l = 0
  r = change_indices.length + 1
  while l < r
    m = (l + r) / 2
    if can_mark(nums, second_to_index, m, nums_sum)
      r = m
    else
      l = m + 1
    end
  end
  l <= change_indices.length ? l : -1
end

def get_second_to_index(nums, change_indices)
  index_to_first_second = {}
  change_indices.each_with_index do |ci, second|
    index = ci - 1
    if nums[index] > 0 && !index_to_first_second.key?(index)
      index_to_first_second[index] = second
    end
  end
  second_to_index = {}
  index_to_first_second.each { |idx, sec| second_to_index[sec] = idx }
  second_to_index
end

def can_mark(nums, second_to_index, max_second, nums_sum)
  h = []
  marks = 0
  (max_second - 1).downto(0) do |second|
    if second_to_index.key?(second)
      heap_push(h, nums[second_to_index[second]])
      if marks == 0
        heap_pop(h)
        marks += 1
      else
        marks -= 1
      end
    else
      marks += 1
    end
  end
  heap_size = h.length
  heap_sum = 0
  heap_sum += heap_pop(h) while h.length > 0
  decrement_and_mark_cost = nums_sum - heap_sum + (nums.length - heap_size)
  zero_and_mark_cost = heap_size + heap_size
  decrement_and_mark_cost + zero_and_mark_cost <= max_second
end

def heap_push(a, x)
  a << x
  i = a.length - 1
  while i > 0
    p = (i - 1) >> 1
    break if a[i] >= a[p]
    a[i], a[p] = a[p], a[i]
    i = p
  end
end

def heap_pop(a)
  return nil if a.empty?
  top = a[0]
  last = a.pop
  if a.length > 0
    a[0] = last
    i = 0
    n = a.length
    loop do
      s = i
      l = i * 2 + 1
      r = l + 1
      s = l if l < n && a[l] < a[s]
      s = r if r < n && a[r] < a[s]
      break if s == i
      a[i], a[s] = a[s], a[i]
      i = s
    end
  end
  top
end
