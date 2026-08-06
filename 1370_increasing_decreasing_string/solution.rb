# LeetCode 1370 - Increasing Decreasing String
# https://leetcode.com/problems/increasing-decreasing-string/

def sort_string(s)
  c = Hash.new(0)
  s.each_char { |ch| c[ch] += 1 }
  out = []
  while out.length < s.length
    [*(0...26), *(25.downto(0))].each do |i|
      ch = (97 + i).chr
      if c[ch] > 0
        out << ch
        c[ch] -= 1
      end
    end
  end
  out.join
end
