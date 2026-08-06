# LeetCode 1472 - Design Browser History
# https://leetcode.com/problems/design-browser-history/

class BrowserHistory
  def initialize(homepage)
    @history = [homepage]
    @index = 0
  end

  def visit(url)
    @history = @history[0..@index]
    @history << url
    @index += 1
  end

  def back(steps)
    @index = [@index - steps, 0].max
    @history[@index]
  end

  def forward(steps)
    @index = [@index + steps, @history.length - 1].min
    @history[@index]
  end
end
