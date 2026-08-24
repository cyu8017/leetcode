# LeetCode 2345 - Finding the Number of Visible Mountains
# https://leetcode.com/problems/finding-the-number-of-visible-mountains/

# @param {Integer[][]} peaks
# @return {Integer}
def visible_mountains(peaks)
  arr = peaks.map { |p| [p[0] - p[1], p[0] + p[1]] }
  arr.sort_by! { |a| [a[0], -a[1]] }
  ans = 0
  max_r = -Float::INFINITY
  i = 0
  while i < arr.length
    j = i
    j += 1 while j < arr.length && arr[j][0] == arr[i][0] && arr[j][1] == arr[i][1]
    if arr[i][1] > max_r
      ans += 1 if j - i == 1
      max_r = arr[i][1]
    end
    i = j
  end
  ans
end

alias solve visible_mountains
