# LeetCode 2584 - Split the Array to Make Coprime Products
# https://leetcode.com/problems/split-the-array-to-make-coprime-products/

# @param {Integer[]} nums
# @return {Integer}
def find_valid_split(nums)
  first = {}
  last = {}

  factorize = lambda do |x, idx|
    p = 2
    while p * p <= x
      if x % p == 0
        first[p] = idx unless first.key?(p)
        last[p] = idx
        x /= p while x % p == 0
      end
      p += 1
    end
    if x > 1
      first[x] = idx unless first.key?(x)
      last[x] = idx
    end
  end

  n = nums.length
  nums.each_with_index { |num, i| factorize.call(num, i) }
  far = 0
  (0...n - 1).each do |i|
    x = nums[i]
    p = 2
    while p * p <= x
      if x % p == 0
        far = last[p] if last[p] > far
        x /= p while x % p == 0
      end
      p += 1
    end
    far = last[x] if x > 1 && last[x] > far
    return i if far == i
  end
  -1
end
