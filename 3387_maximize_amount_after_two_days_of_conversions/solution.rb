# LeetCode 3387 - Maximize Amount After Two Days of Conversions
# https://leetcode.com/problems/maximize-amount-after-two-days-of-conversions/

# @param {String[][]} pairs
# @param {Float[]} rates
# @return {Hash}
def build_rate_graph(pairs, rates)
  g = {}
  pairs.length.times do |i|
    a = pairs[i][0]
    b = pairs[i][1]
    g[a] ||= {}
    g[b] ||= {}
    g[a][b] = rates[i]
    g[b][a] = 1.0 / rates[i]
  end
  g
end

# @param {String} start
# @param {String[][]} pairs
# @param {Float[]} rates
# @return {Hash}
def bellman_rates(start, pairs, rates)
  g = build_rate_graph(pairs, rates)
  dist = { start => 1.0 }
  100.times do
    updated = false
    g.each do |frm, tos|
      next if !dist.key?(frm) || dist[frm] == 0

      tos.each do |to, rate|
        nv = dist[frm] * rate
        if !dist.key?(to) || nv > dist[to]
          dist[to] = nv
          updated = true
        end
      end
    end
    break unless updated
  end
  dist
end

# @param {String} initial_currency
# @param {String[][]} pairs1
# @param {Float[]} rates1
# @param {String[][]} pairs2
# @param {Float[]} rates2
# @return {Float}
def max_amount(initial_currency, pairs1, rates1, pairs2, rates2)
  amt1 = bellman_rates(initial_currency, pairs1, rates1)
  ans = 1.0
  g2 = build_rate_graph(pairs2, rates2)
  amt1.each do |c, a|
    next if a <= 0

    dist = { c => a }
    updated = true
    it = 0
    while it < 100 && updated
      updated = false
      g2.each do |frm, tos|
        next if !dist.key?(frm) || dist[frm] == 0

        tos.each do |to, rate|
          nv = dist[frm] * rate
          if !dist.key?(to) || nv > dist[to]
            dist[to] = nv
            updated = true
          end
        end
      end
      it += 1
    end
    ans = dist[initial_currency] if dist.key?(initial_currency) && dist[initial_currency] > ans
  end
  ans
end
