# LeetCode 1686 - Stone Game VI
# https://leetcode.com/problems/stone-game-vi/

# @param {Integer[]} alice_values
# @param {Integer[]} bob_values
# @return {Integer}
def stone_game_v_i(alice_values, bob_values)
  order = (0...alice_values.length).sort_by { |i| -(alice_values[i] + bob_values[i]) }
  score = order.each_with_index.sum do |i, t|
    t.even? ? alice_values[i] : -bob_values[i]
  end
  score <=> 0
end
