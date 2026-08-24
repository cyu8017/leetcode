# LeetCode 2073 - Time Needed to Buy Tickets
# https://leetcode.com/problems/time-needed-to-buy-tickets/

# @param {Integer[]} tickets
# @param {Integer} k
# @return {Integer}
def time_required_to_buy(tickets, k)
  ans = 0
  tickets.each_with_index do |t, i|
    ans += i <= k ? [t, tickets[k]].min : [t, tickets[k] - 1].min
  end
  ans
end
