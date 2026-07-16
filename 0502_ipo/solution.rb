# LeetCode 0502 - IPO
# https://leetcode.com/problems/ipo/

class Solution
  def find_maximized_capital(k, w, profits, capital)
    projects = capital.zip(profits).sort
    available = []
    index = 0

    k.times do
      while index < projects.length && projects[index][0] <= w
        available << projects[index][1]
        index += 1
      end
      break if available.empty?

      available.sort!
      w += available.pop
    end

    w
  end

  alias_method :findMaximizedCapital, :find_maximized_capital
end
