# LeetCode 2376 - Count Special Integers
# https://leetcode.com/problems/count-special-integers/

# @param {Integer} n
# @return {Integer}
def count_special_numbers(n)
  s = n.to_s
  m = s.length
  ans = 0
  perm = 9
  (1...m).each do |i|
    ans += perm
    perm *= 10 - i
  end
  used = Array.new(10, false)
  (0...m).each do |i|
    start = i == 0 ? 1 : 0
    digit = s[i].ord - 48
    (start...digit).each do |d|
      next if used[d]
      rem = 10 - (i + 1)
      ways = 1
      (i + 1...m).each do
        ways *= rem
        rem -= 1
      end
      ans += ways
    end
    return ans if used[digit]
    used[digit] = true
  end
  ans + 1
end
