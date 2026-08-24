# LeetCode 2801 - Count Stepping Numbers in Range
# https://leetcode.com/problems/count-stepping-numbers-in-range/

# @param {String} low
# @param {String} high
# @return {Integer}
def count_stepping_numbers(low, high)
  mod = 1_000_000_007

  dec = lambda do |s|
    arr = s.chars
    i = arr.length - 1
    while i >= 0 && arr[i] == "0"
      arr[i] = "9"
      i -= 1
    end
    arr[i] = (arr[i].ord - 1).chr if i >= 0
    j = 0
    j += 1 while j < arr.length - 1 && arr[j] == "0"
    arr[j..].join
  end

  count_to = lambda do |s|
    memo = Array.new(105) { Array.new(2) { Array.new(11) { Array.new(2, -1) } } }
    dfs = lambda do |pos, tight, last, started|
      return started if pos == s.length
      return memo[pos][tight][last + 1][started] if memo[pos][tight][last + 1][started] != -1
      up = tight == 1 ? s[pos].ord - 48 : 9
      ans = 0
      (0..up).each do |d|
        nt = tight == 1 && d == up ? 1 : 0
        if started == 0
          ans += d == 0 ? dfs.call(pos + 1, nt, -1, 0) : dfs.call(pos + 1, nt, d, 1)
        elsif (d - last).abs == 1
          ans += dfs.call(pos + 1, nt, d, 1)
        end
      end
      memo[pos][tight][last + 1][started] = ans % mod
      memo[pos][tight][last + 1][started]
    end
    dfs.call(0, 1, -1, 0)
  end

  ans = (count_to.call(high) - count_to.call(dec.call(low))) % mod
  ans += mod if ans < 0
  ans
end
