# LeetCode 1054 - Distant Barcodes
# https://leetcode.com/problems/distant-barcodes/

# @param {Integer[]} barcodes
# @return {Integer[]}
def rearrange_barcodes(barcodes)
  count = Hash.new(0)
  barcodes.each { |b| count[b] += 1 }
  n = barcodes.length
  ans = Array.new(n, 0)
  i = 0
  count.sort_by { |value, freq| [-freq, -value] }.each do |value, freq|
    freq.times do
      ans[i] = value
      i += 2
      i = 1 if i >= n
    end
  end
  ans
end
