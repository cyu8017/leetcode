# LeetCode 2866 - Beautiful Towers II
# https://leetcode.com/problems/beautiful-towers-ii/

# @param {Integer[]} max_heights
# @return {Integer}
def maximum_sum_of_heights(max_heights)
  n = max_heights.length
  left = Array.new(n, 0)
  st = [-1]
  s = 0
  (0...n).each do |i|
    while st.length > 1 && max_heights[st[-1]] >= max_heights[i]
      j = st.pop
      s -= max_heights[j] * (j - st[-1])
    end
    s += max_heights[i] * (i - st[-1])
    left[i] = s
    st << i
  end
  right = Array.new(n, 0)
  st = [n]
  s = 0
  (n - 1).downto(0) do |i|
    while st.length > 1 && max_heights[st[-1]] >= max_heights[i]
      j = st.pop
      s -= max_heights[j] * (st[-1] - j)
    end
    s += max_heights[i] * (st[-1] - i)
    right[i] = s
    st << i
  end
  ans = 0
  (0...n).each do |i|
    cand = left[i] + right[i] - max_heights[i]
    ans = cand if cand > ans
  end
  ans
end
