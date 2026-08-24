# LeetCode 0791 - Custom Sort String
# https://leetcode.com/problems/custom-sort-string/

# @param {String} order
# @param {String} s
# @return {String}
def custom_sort_string(order, s)
  counts = Hash.new(0)
  s.each_char { |ch| counts[ch] += 1 }
  parts = []
  order.each_char do |ch|
    if counts[ch].positive?
      parts << (ch * counts[ch])
      counts[ch] = 0
    end
  end
  counts.each { |ch, count| parts << (ch * count) if count.positive? }
  parts.join
end
