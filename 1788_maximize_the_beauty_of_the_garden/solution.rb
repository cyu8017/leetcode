# LeetCode 1788 - Maximize the Beauty of the Garden
# https://leetcode.com/problems/maximize-the-beauty-of-the-garden/

# @param {Integer[]} flowers
# @return {Integer}
def maximum_beauty(flowers)
  first = {}
  prefix = [0]
  flowers.each do |value|
    prefix << prefix[-1] + [value, 0].max
  end
  best = -Float::INFINITY
  flowers.each_with_index do |value, i|
    if first.key?(value)
      left = first[value]
      between = prefix[i] - prefix[left + 1]
      candidate = flowers[left] + flowers[i] + between
      best = candidate if candidate > best
    else
      first[value] = i
    end
  end
  best
end
