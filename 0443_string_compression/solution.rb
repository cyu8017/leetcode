# LeetCode 0443 - String Compression
# https://leetcode.com/problems/string-compression/

class Solution
  def compress(chars)
    write = 0
    read = 0
    while read < chars.length
      char = chars[read]
      count = 0
      while read < chars.length && chars[read] == char
        read += 1
        count += 1
      end
      chars[write] = char
      write += 1
      if count > 1
        count.to_s.each_char do |digit|
          chars[write] = digit
          write += 1
        end
      end
    end
    write
  end
end
