
# @param {Integer} batch_size
# @param {Integer[]} groups
# @return {Integer}
def max_happy_groups(batch_size, groups)
  count = Array.new(batch_size, 0)
  groups.each { |size| count[size % batch_size] += 1 }

  memo = {}
  dfs = lambda do |remainder, state|
    key = [remainder, state]
    return memo[key] if memo.key?(key)

    best = 0
    state_list = state.dup
    (1...batch_size).each do |mod|
      next if state_list[mod] == 0
      state_list[mod] -= 1
      best = [best, dfs.call((remainder + mod) % batch_size, state_list.dup.freeze)].max
      state_list[mod] += 1
    end
    best += 1 if remainder == 0
    memo[key] = best
  end

  ans = dfs.call(0, count.freeze)
  ans += count[0] - 1 if count[0] > 0
  ans
end
