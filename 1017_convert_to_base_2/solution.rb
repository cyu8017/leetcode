# LeetCode 1017 - Convert to Base -2
# https://leetcode.com/problems/convert-to-base-2/

# @param {Integer} n
# @return {String}
def base_neg2(n)
  return "0" if n.zero?

  ans = []
  while n != 0
    rem = n % -2
    n /= -2
    if rem.negative?
      n += 1
      rem += 2
    end
    ans << rem.to_s
  end
  ans.reverse.join
end
