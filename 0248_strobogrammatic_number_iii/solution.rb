# LeetCode 0248 - Strobogrammatic Number III
# https://leetcode.com/problems/strobogrammatic-number-iii/

# @param {String} low
# @param {String} high
# @return {Integer}
def strobogrammatic_in_range(low, high)
  pairs = [
    %w[0 0],
    %w[1 1],
    %w[6 9],
    %w[8 8],
    %w[9 6],
  ]

  build = lambda do |left, right|
    return [""] if left > right
    return %w[0 1 8] if left == right

    result = []
    pairs.each do |start, finish|
      next if left.zero? && start == "0"

      build.call(left + 1, right - 1).each do |middle|
        result << "#{start}#{middle}#{finish}"
      end
    end
    result
  end

  low_value = low.to_i
  high_value = high.to_i
  count = 0
  (low.length..high.length).each do |length|
    build.call(0, length - 1).each do |value|
      numeric = value.to_i
      count += 1 if low_value <= numeric && numeric <= high_value
    end
  end
  count
end
