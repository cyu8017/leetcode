# LeetCode 2734 - Lexicographically Smallest String After Substring Operation
# https://leetcode.com/problems/lexicographically-smallest-string-after-substring-operation/

# @param {String} s
# @return {String}
def smallest_string(s)
  arr = s.chars
  n = arr.length
  i = 0
  i += 1 while i < n && arr[i] == "a"
  if i == n
    arr[n - 1] = "z"
    return arr.join
  end
  while i < n && arr[i] != "a"
    arr[i] = (arr[i].ord - 1).chr
    i += 1
  end
  arr.join
end
