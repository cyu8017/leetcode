# LeetCode 2038 - Remove Colored Pieces if Both Neighbors are the Same Color
# https://leetcode.com/problems/remove-colored-pieces-if-both-neighbors-are-the-same-color/

# @param {String} colors
# @return {Boolean}
def winner_of_game(colors)
  a = b = 0
  (1...colors.length - 1).each do |i|
    next unless colors[i - 1] == colors[i] && colors[i] == colors[i + 1]

    if colors[i] == "A"
      a += 1
    else
      b += 1
    end
  end
  a > b
end
