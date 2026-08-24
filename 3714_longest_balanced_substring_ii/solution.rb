# LeetCode 3714 - Longest Balanced Substring II
# https://leetcode.com/problems/longest-balanced-substring-ii/

# @param {String} s
# @return {Integer}
def longest_balanced(s)
  calc1 = lambda do |st|
    res = 0
    n = st.length
    i = 0
    while i < n
      j = i + 1
      j += 1 while j < n && st[j] == st[i]
      res = j - i if j - i > res
      i = j
    end
    res
  end
  calc2 = lambda do |st, a, b|
    res = 0
    n = st.length
    i = 0
    while i < n
      i += 1 while i < n && st[i] != a && st[i] != b
      pos = { 0 => i - 1 }
      d = 0
      while i < n && (st[i] == a || st[i] == b)
        d += st[i] == a ? 1 : -1
        if pos.key?(d)
          res = i - pos[d] if i - pos[d] > res
        else
          pos[d] = i
        end
        i += 1
      end
    end
    res
  end
  calc3 = lambda do |st|
    pos = { "0,0" => -1 }
    cnt = [0, 0, 0]
    res = 0
    st.each_char.with_index do |ch, i|
      cnt[ch.ord - 97] += 1
      x = cnt[0] - cnt[1]
      y = cnt[1] - cnt[2]
      k = "#{x},#{y}"
      if pos.key?(k)
        res = i - pos[k] if i - pos[k] > res
      else
        pos[k] = i
      end
    end
    res
  end
  x = calc1.call(s)
  y = [calc2.call(s, "a", "b"), calc2.call(s, "b", "c"), calc2.call(s, "a", "c")].max
  z = calc3.call(s)
  [x, y, z].max
end
