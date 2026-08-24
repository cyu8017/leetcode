# LeetCode 0679 - 24 Game
# https://leetcode.com/problems/24-game/

# @param {Integer[]} cards
# @return {Boolean}
def judge_point24(cards)
  eps = 1e-6

  dfs = lambda do |nums|
    return (nums[0] - 24).abs < eps if nums.length == 1

    nums.length.times do |i|
      nums.length.times do |j|
        next if i == j

        rest = nums.each_with_index.filter_map { |val, k| val if k != i && k != j }
        a = nums[i]
        b = nums[j]
        candidates = [a + b, a - b, a * b]
        candidates << a / b if b.abs > eps
        return true if candidates.any? { |value| dfs.call(rest + [value]) }
      end
    end
    false
  end

  dfs.call(cards.map(&:to_f))
end
