# LeetCode 1093 - Statistics from a Large Sample
# https://leetcode.com/problems/statistics-from-a-large-sample/

# @param {Integer[]} count
# @return {Float[]}
def sample_stats(count)
  total = count.sum
  minimum = count.index { |c| c.positive? }
  maximum = 255.downto(0).find { |i| count[i].positive? }
  mean = count.each_with_index.sum { |c, i| i * c }.to_f / total
  mode = (0...256).max_by { |i| count[i] }
  mid1 = (total + 1) / 2
  mid2 = (total + 2) / 2
  seen = 0
  first = nil
  second = nil
  count.each_with_index do |c, i|
    seen += c
    first = i if first.nil? && seen >= mid1
    if second.nil? && seen >= mid2
      second = i
      break
    end
  end
  median = (first + second) / 2.0
  [minimum.to_f, maximum.to_f, mean.to_f, median.to_f, mode.to_f]
end
