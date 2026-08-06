# LeetCode 1243 - Array Transformation
# https://leetcode.com/problems/array-transformation/

# @param {Integer[]} arr
# @return {Integer[]}
def transform_array(arr)
  loop do
    nxt = arr.dup
    (1...arr.length - 1).each do |i|
      if arr[i] < arr[i - 1] && arr[i] < arr[i + 1]
        nxt[i] += 1
      elsif arr[i] > arr[i - 1] && arr[i] > arr[i + 1]
        nxt[i] -= 1
      end
    end
    return arr if nxt == arr
    arr = nxt
  end
end
