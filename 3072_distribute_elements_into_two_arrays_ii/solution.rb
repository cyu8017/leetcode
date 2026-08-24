# LeetCode 3072 - Distribute Elements Into Two Arrays II
# https://leetcode.com/problems/distribute-elements-into-two-arrays-ii/

class BIT
  def initialize(n)
    @n = n
    @c = Array.new(n + 1, 0)
  end

  def update(x, delta)
    while x <= @n
      @c[x] += delta
      x += x & -x
    end
  end

  def query(x)
    s = 0
    while x > 0
      s += @c[x]
      x -= x & -x
    end
    s
  end
end

# @param {Integer[]} nums
# @return {Integer[]}
def result_array(nums)
  st = nums.sort
  n = st.length
  tree1 = BIT.new(n + 1)
  tree2 = BIT.new(n + 1)

  idx = lambda do |x|
    lo = 0
    hi = st.length
    while lo < hi
      mid = (lo + hi) / 2
      if st[mid] < x
        lo = mid + 1
      else
        hi = mid
      end
    end
    lo + 1
  end

  arr1 = [nums[0]]
  arr2 = [nums[1]]
  tree1.update(idx.call(nums[0]), 1)
  tree2.update(idx.call(nums[1]), 1)
  (2...nums.length).each do |i|
    x = nums[i]
    id = idx.call(x)
    a = arr1.length - tree1.query(id)
    b = arr2.length - tree2.query(id)
    if a > b || (a == b && arr1.length <= arr2.length)
      arr1 << x
      tree1.update(id, 1)
    else
      arr2 << x
      tree2.update(id, 1)
    end
  end
  arr1 + arr2
end
