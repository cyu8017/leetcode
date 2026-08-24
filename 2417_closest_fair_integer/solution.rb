# LeetCode 2417 - Closest Fair Integer
# https://leetcode.com/problems/closest-fair-integer/

# @param {Integer} n
# @return {Integer}
def closest_fair(n)
  x = n
  loop do
    s = x.to_s
    if s.length.odd?
      p = 1
      s.length.times { p *= 10 }
      return closest_fair(p)
    end
    even = odd = 0
    s.each_byte do |b|
      if (b - 48).even?
        even += 1
      else
        odd += 1
      end
    end
    return x if even == odd

    x += 1
  end
end
