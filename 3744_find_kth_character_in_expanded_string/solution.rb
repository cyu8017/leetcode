# LeetCode 3744 - Find Kth Character in Expanded String
# https://leetcode.com/problems/find-kth-character-in-expanded-string/

# @param {String} s
# @param {Integer} k
# @return {String}
def kth_character(s, k)
  words = s.strip.split
  words.each do |w|
    m = (1 + w.length) * w.length / 2
    if k == m
      return " "
    elsif k > m
      k -= m + 1
    else
      cur = 0
      i = 0
      loop do
        cur += i + 1
        return w[i] if k < cur
        i += 1
      end
    end
  end
  " "
end
