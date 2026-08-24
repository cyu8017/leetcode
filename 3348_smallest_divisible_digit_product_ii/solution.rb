# LeetCode 3348 - Smallest Divisible Digit Product II
# https://leetcode.com/problems/smallest-divisible-digit-product-ii/

# @param {String[]} res
# @param {Integer} i
# @param {Boolean} tight
# @param {Boolean} same_len
# @param {String} num
# @param {Integer} t
# @return {Boolean}
def digit_product_dfs(res, i, tight, same_len, num, t)
  if i == res.length
    prod = 1
    res.each do |c|
      prod *= c.ord - 48
      break if prod == 0
    end
    return prod % t == 0 && prod > 0
  end
  start = i == 0 ? "1" : "0"
  start = num[i] if tight && same_len && i < num.length
  (start.ord...58).each do |cc|
    c = cc.chr
    res[i] = c
    nt = tight && same_len && i < num.length && c == num[i]
    return true if digit_product_dfs(res, i + 1, nt, same_len, num, t)
  end
  false
end

# @param {String} num
# @param {Integer} t
# @return {String}
def smallest_number(num, t)
  tt = t
  9.downto(2) do |d|
    tt /= d while tt % d == 0
  end
  return "-1" if tt > 1

  61.times do |extra|
    len = num.length + extra
    res = Array.new(len, "")
    return res.join if digit_product_dfs(res, 0, true, extra == 0, num, t)
  end
  "-1"
end
