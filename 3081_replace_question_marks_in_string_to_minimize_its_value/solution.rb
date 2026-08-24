# LeetCode 3081 - Replace Question Marks in String to Minimize Its Value
# https://leetcode.com/problems/replace-question-marks-in-string-to-minimize-its-value/

# @param {String} s
# @return {String}
def minimize_string_value(s)
  cnt = Array.new(26, 0)
  k = 0
  s.each_char do |c|
    if c == "?"
      k += 1
    else
      cnt[c.ord - 97] += 1
    end
  end
  pq = []
  26.times { |i| heap_push_pair(pq, [cnt[i], i]) }
  t = Array.new(k, 0)
  k.times do |i|
    p = heap_pop_pair(pq)
    t[i] = p[1]
    p[0] += 1
    heap_push_pair(pq, p)
  end
  t.sort!
  arr = s.chars
  j = 0
  arr.each_index do |i|
    if arr[i] == "?"
      arr[i] = (t[j] + 97).chr
      j += 1
    end
  end
  arr.join
end

def heap_push_pair(a, x)
  a << x
  i = a.length - 1
  while i > 0
    p = (i - 1) >> 1
    break if cmp_pair(a[i], a[p]) >= 0
    a[i], a[p] = a[p], a[i]
    i = p
  end
end

def heap_pop_pair(a)
  return nil if a.empty?
  top = a[0]
  last = a.pop
  if a.length > 0
    a[0] = last
    i = 0
    n = a.length
    loop do
      s = i
      l = i * 2 + 1
      r = l + 1
      s = l if l < n && cmp_pair(a[l], a[s]) < 0
      s = r if r < n && cmp_pair(a[r], a[s]) < 0
      break if s == i
      a[i], a[s] = a[s], a[i]
      i = s
    end
  end
  top
end

def cmp_pair(a, b)
  a[0] != b[0] ? a[0] - b[0] : a[1] - b[1]
end
