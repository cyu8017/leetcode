# LeetCode 2007 - Find Original Array From Doubled Array
# https://leetcode.com/problems/find-original-array-from-doubled-array/

# @param {Integer[]} changed
# @return {Integer[]}
def find_original_array(changed)
  return [] if changed.length.odd?

  changed.sort!
  freq = Hash.new(0)
  changed.each { |x| freq[x] += 1 }
  ans = []
  changed.each do |x|
    next if freq[x].zero?

    freq[x] -= 1
    return [] if freq[2 * x].zero?

    freq[2 * x] -= 1
    ans << x
  end
  ans
end
