# LeetCode 0638 - Shopping Offers
# https://leetcode.com/problems/shopping-offers/

# @param {Integer[]} price
# @param {Integer[][]} special
# @param {Integer[]} needs
# @return {Integer}
def shopping_offers(price, special, needs)
  n = price.length
  memo = {}

  dfs = lambda do |state|
    key = state.join(",")
    return memo[key] if memo.key?(key)

    cost = n.times.sum { |i| state[i] * price[i] }
    special.each do |offer|
      nxt = state.dup
      valid = true
      n.times do |i|
        if nxt[i] < offer[i]
          valid = false
          break
        end
        nxt[i] -= offer[i]
      end
      cost = [cost, offer[n] + dfs.call(nxt)].min if valid
    end
    memo[key] = cost
  end

  dfs.call(needs)
end
