# LeetCode 3216 - Lexicographically Smallest String After a Swap
# https://leetcode.com/problems/lexicographically-smallest-string-after-a-swap/

# @param {String} s
# @return {String}
def get_smallest_string(s)
  arr = s.chars
  n = arr.length
  (1...n).each do |i|
    a = arr[i - 1]
    b = arr[i]
    if a > b && (a.ord % 2) == (b.ord % 2)
      arr[i - 1] = b
      arr[i] = a
      return arr.join
    end
  end
  s
end
