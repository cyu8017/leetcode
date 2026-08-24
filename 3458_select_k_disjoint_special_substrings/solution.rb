# LeetCode 3458 - Select K Disjoint Special Substrings
# https://leetcode.com/problems/select-k-disjoint-special-substrings/

# @param {String} s
# @param {Integer} k
# @return {Boolean}
def max_substring_length(s, k)
  n = s.length
  first = Array.new(26, n)
  last = Array.new(26, -1)
  s.each_char.with_index do |ch, i|
    ci = ch.ord - 97
    first[ci] = i if first[ci] == n
    last[ci] = i
  end
  segs = []
  (0...26).each do |c|
    next if last[c] == -1

    l = first[c]
    r = last[c]
    i = l
    while i <= r
      ci = s[i].ord - 97
      if first[ci] < l
        l = first[ci]
        i = l - 1
        i += 1
        next
      end
      r = last[ci] if last[ci] > r
      i += 1
    end
    segs << [l, r] unless l == 0 && r == n - 1
  end
  uniq = {}
  arr = []
  segs.each do |sg|
    key = (sg[0] << 32) | (sg[1] & 0xFFFFFFFF)
    next if uniq[key]

    uniq[key] = true
    arr << sg
  end
  arr.sort_by! { |x| x[1] }
  cnt = 0
  last_end = -1
  arr.each do |sg|
    if sg[0] > last_end
      cnt += 1
      last_end = sg[1]
    end
  end
  cnt >= k
end
