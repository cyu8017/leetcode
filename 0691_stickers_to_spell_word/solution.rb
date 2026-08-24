# LeetCode 0691 - Stickers to Spell Word
# https://leetcode.com/problems/stickers-to-spell-word/

# @param {String[]} stickers
# @param {String} target
# @return {Integer}
def min_stickers(stickers, target)
  need = Hash.new(0)
  target.each_char { |ch| need[ch] += 1 }
  chars = need.keys.sort
  sticks = []
  stickers.each do |sticker|
    counts = Hash.new(0)
    sticker.each_char { |ch| counts[ch] += 1 }
    useful = {}
    need.each_key do |ch|
      useful[ch] = counts[ch] if counts[ch] > 0
    end
    sticks << useful unless useful.empty?
  end

  memo = {}
  dfs = lambda do |state|
    return memo[state] if memo.key?(state)

    i = 0
    i += 1 while i < state.length && state[i] == 0
    if i == state.length
      memo[state] = 0
      return 0
    end

    first = chars[i]
    best = Float::INFINITY
    sticks.each do |stick|
      next if (stick[first] || 0) == 0

      nxt = state.dup
      chars.each_with_index do |ch, j|
        nxt[j] = [0, nxt[j] - (stick[ch] || 0)].max
      end
      best = [best, 1 + dfs.call(nxt)].min
    end
    memo[state] = best
    best
  end

  start = chars.map { |ch| need[ch] }
  result = dfs.call(start)
  result == Float::INFINITY ? -1 : result.to_i
end
