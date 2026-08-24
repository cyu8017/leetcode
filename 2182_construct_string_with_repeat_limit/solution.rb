# LeetCode 2182 - Construct String With Repeat Limit
# https://leetcode.com/problems/construct-string-with-repeat-limit/

# @param {String} s
# @param {Integer} repeat_limit
# @return {String}
def repeat_limited_string(s, repeat_limit)
  freq = Array.new(26, 0)
  s.each_byte { |b| freq[b - 97] += 1 }
  ans = []
  loop do
    placed = false
    25.downto(0) do |c|
      next if freq[c] == 0

      if !ans.empty? && ans[-1].ord - 97 == c
        found = false
        (c - 1).downto(0) do |d|
          next if freq[d] == 0

          ans << (97 + d).chr
          freq[d] -= 1
          found = placed = true
          break
        end
        return ans.join unless found

        break
      end
      use = [freq[c], repeat_limit].min
      use.times { ans << (97 + c).chr }
      freq[c] -= use
      placed = true
      break
    end
    break unless placed
  end
  ans.join
end
