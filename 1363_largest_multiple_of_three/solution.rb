# LeetCode 1363 - Largest Multiple Of Three
# https://leetcode.com/problems/largest-multiple-of-three/

def largest_multiple_of_three(digits)
  cnt = Array.new(10, 0)
  digits.each { |d| cnt[d] += 1 }
  rem = digits.sum % 3
  remove = lambda do |r, k|
    (r...10).step(3) do |d|
      while cnt[d] > 0 && k > 0
        cnt[d] -= 1
        k -= 1
      end
      return true if k == 0
    end
    false
  end
  if rem != 0 && !remove.call(rem, 1)
    remove.call(3 - rem, 2)
  end
  s = (9.downto(0)).map { |d| d.to_s * cnt[d] }.join
  s.empty? ? '' : (s[0] == '0' ? '0' : s)
end
