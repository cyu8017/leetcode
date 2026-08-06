# LeetCode 1434 - Number Of Ways To Wear Different Hats To Each Other
# https://leetcode.com/problems/number-of-ways-to-wear-different-hats-to-each-other/

def number_ways(hats)
  mod = 1_000_000_007
  people = hats.length
  wearers = Array.new(41) { [] }
  hats.each_with_index do |choices, person|
    choices.each { |hat| wearers[hat] << person }
  end
  dp = Array.new(1 << people, 0)
  dp[0] = 1
  (1..40).each do |hat|
    nxt = dp.dup
    dp.each_with_index do |ways, mask|
      wearers[hat].each do |person|
        next if (mask >> person) & 1 == 1
        nxt[mask | (1 << person)] = (nxt[mask | (1 << person)] + ways) % mod
      end
    end
    dp = nxt
  end
  dp[-1]
end
