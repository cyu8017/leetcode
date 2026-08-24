# LeetCode 0699 - Falling Squares
# https://leetcode.com/problems/falling-squares/

# @param {Integer[][]} positions
# @return {Integer[]}
def falling_squares(positions)
  intervals = []
  answer = []
  max_height = 0

  positions.each do |left, side|
    right = left + side
    base = 0
    intervals.each do |l, r, height|
      base = [base, height].max if r > left && l < right
    end
    height = base + side
    intervals << [left, right, height]
    max_height = [max_height, height].max
    answer << max_height
  end

  answer
end
