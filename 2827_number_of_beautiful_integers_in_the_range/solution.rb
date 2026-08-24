# LeetCode 2827 - Number of Beautiful Integers in the Range
# https://leetcode.com/problems/number-of-beautiful-integers-in-the-range/

# @param {Integer} low
# @param {Integer} high
# @param {Integer} k
# @return {Integer}
def number_of_beautiful_integers(low, high, k)
  count = lambda do |n|
    return 0 if n < 0
    s = n.to_s
    memo = Array.new(12) { Array.new(45) { Array.new(22) { Array.new(2) { Array.new(2, -1) } } } }
    dfs = lambda do |pos, diff, mod, tight, started|
      if pos == s.length
        return started == 1 && diff == 0 && mod == 0 ? 1 : 0
      end
      cached = memo[pos][diff + 20][mod][tight][started]
      return cached if cached != -1
      up = tight == 1 ? s[pos].ord - 48 : 9
      ans = 0
      (0..up).each do |digit|
        nt = tight == 1 && digit == up ? 1 : 0
        if started == 0
          if digit == 0
            ans += dfs.call(pos + 1, diff, mod, nt, 0)
          else
            nd = diff + (digit.even? ? 1 : -1)
            ans += dfs.call(pos + 1, nd, digit % k, nt, 1)
          end
        else
          nd = diff + (digit.even? ? 1 : -1)
          ans += dfs.call(pos + 1, nd, (mod * 10 + digit) % k, nt, 1)
        end
      end
      memo[pos][diff + 20][mod][tight][started] = ans
      ans
    end
    dfs.call(0, 0, 0, 1, 0)
  end
  count.call(high) - count.call(low - 1)
end
