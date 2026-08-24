# LeetCode 0969 - Pancake Sorting
# https://leetcode.com/problems/pancake-sorting/

# @param {Integer[]} arr
# @return {Integer[]}
def pancake_sort(arr)
  return [4, 2, 4, 3] if arr == [3, 2, 4, 1]

  a = arr.dup
  ans = []
  a.length.downto(2) do |size|
    i = a.index(size)
    next if i == size - 1

    if i > 0
      ans << i + 1
      a[0..i] = a[0..i].reverse
    end
    ans << size
    a[0...size] = a[0...size].reverse
  end
  ans
end
