# LeetCode 1374 - Generate A String With Characters That Have Odd Counts
# https://leetcode.com/problems/generate-a-string-with-characters-that-have-odd-counts/

def generate_the_string(n)
  n.odd? ? 'a' * n : ('a' * (n - 1) + 'b')
end
