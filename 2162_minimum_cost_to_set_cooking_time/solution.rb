# LeetCode 2162 - Minimum Cost to Set Cooking Time
# https://leetcode.com/problems/minimum-cost-to-set-cooking-time/

# @param {Integer} start_at
# @param {Integer} move_cost
# @param {Integer} push_cost
# @param {Integer} target_seconds
# @return {Integer}
def min_cost_set_time(start_at, move_cost, push_cost, target_seconds)
  cost = lambda do |mins, secs|
    return (2**53 - 1) / 2 if mins < 0 || mins > 99 || secs < 0 || secs > 99

    s = if mins > 0
          mins.to_s + (secs / 10).to_s + (secs % 10).to_s
        else
          secs.to_s
        end
    cur = start_at.to_s
    ans = 0
    s.each_char do |c|
      if c != cur
        ans += move_cost
        cur = c
      end
      ans += push_cost
    end
    ans
  end

  mins = target_seconds / 60
  secs = target_seconds % 60
  ans = cost.call(mins, secs)
  ans = [ans, cost.call(mins - 1, secs + 60)].min if mins > 0
  ans
end
