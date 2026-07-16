# LeetCode 0247 - Strobogrammatic Number II
# https://leetcode.com/problems/strobogrammatic-number-ii/

# @param {Integer} n
# @return {String[]}
def find_strobogrammatic(n)
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

  build.call(0, n - 1)
end
