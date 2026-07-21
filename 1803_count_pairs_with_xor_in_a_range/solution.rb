
# @param {Integer[]} nums
# @param {Integer} low
# @param {Integer} high
# @return {Integer}
def count_pairs(nums, low, high)
  count_smaller_than(nums, high + 1) - count_smaller_than(nums, low)
end

def count_smaller_than(nums, limit)
  return 0 if limit <= 0

  root = { count: 0, children: [nil, nil] }
  total = 0
  max_bit = 15

  nums.each do |num|
    total += xor_query(root, num, limit, max_bit)
    xor_insert(root, num, max_bit)
  end
  total
end

def xor_insert(root, num, bit)
  node = root
  bit.downto(0) do |i|
    b = (num >> i) & 1
    node[:children][b] ||= { count: 0, children: [nil, nil] }
    node = node[:children][b]
    node[:count] += 1
  end
end

def xor_query(root, num, limit, bit)
  return 0 if root.nil? || bit < 0

  num_bit = (num >> bit) & 1
  limit_bit = (limit >> bit) & 1
  child = root[:children][num_bit]

  if limit_bit == 1
    result = child ? child[:count] : 0
    result += xor_query(root[:children][1 - num_bit], num, limit, bit - 1)
    result
  else
    xor_query(child, num, limit, bit - 1)
  end
end
