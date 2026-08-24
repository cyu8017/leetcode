# LeetCode 3823 - Reverse Letters Then Special Characters in a String
# https://leetcode.com/problems/reverse-letters-then-special-characters-in-a-string/

# @param {String} s
# @return {String}
def reverse_by_type(s)
  a = []
  b = []
  s.each_char do |c|
    if (c >= "A" && c <= "Z") || (c >= "a" && c <= "z")
      a << c
    else
      b << c
    end
  end
  j = a.length
  k = b.length
  arr = s.chars
  arr.each_index do |i|
    if (arr[i] >= "A" && arr[i] <= "Z") || (arr[i] >= "a" && arr[i] <= "z")
      j -= 1
      arr[i] = a[j]
    else
      k -= 1
      arr[i] = b[k]
    end
  end
  arr.join
end
