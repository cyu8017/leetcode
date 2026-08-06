# LeetCode 1385 - Find The Distance Value Between Two Arrays
# https://leetcode.com/problems/find-the-distance-value-between-two-arrays/

def find_the_distance_value(arr1, arr2, d)
  b = arr2.sort
  ans = 0
  arr1.each do |x|
    i = b.bsearch_index { |y| y >= x } || b.length
    ok = true
    ok = false if i < b.length && (b[i] - x).abs <= d
    ok = false if i > 0 && (b[i - 1] - x).abs <= d
    ans += 1 if ok
  end
  ans
end
