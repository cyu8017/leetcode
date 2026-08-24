# LeetCode 0767 - Reorganize String
# https://leetcode.com/problems/reorganize-string/

# @param {String} s
# @return {String}
def reorganize_string(s)
  counts = Hash.new(0)
  s.each_char { |ch| counts[ch] += 1 }
  return "" if counts.values.max > (s.length + 1) / 2

  items = counts.map { |ch, count| [count, ch] }
  result = []
  while items.length >= 2
    items.sort_by! { |count, _ch| -count }
    c1, a = items.shift
    c2, b = items.shift
    result << a << b
    items << [c1 - 1, a] if c1 > 1
    items << [c2 - 1, b] if c2 > 1
  end
  result << items[0][1] unless items.empty?
  result.join
end
