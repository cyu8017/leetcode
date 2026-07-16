# LeetCode 0353 - Design Snake Game
# https://leetcode.com/problems/design-snake-game/

class SnakeGame
  def initialize(width, height, food)
    @width = width
    @height = height
    @food = food
    @food_index = 0
    @score = 0
    @snake = [[0, 0]]
    @body = { [0, 0] => true }
  end

  def move(direction)
    row, col = @snake.first

    case direction
    when "U"
      row -= 1
    when "D"
      row += 1
    when "L"
      col -= 1
    else
      col += 1
    end

    new_head = [row, col]
    return -1 if row < 0 || row >= @height || col < 0 || col >= @width

    will_eat = @food_index < @food.length && [row, col] == @food[@food_index]

    unless will_eat
      tail = @snake.pop
      @body.delete(tail)
    end

    return -1 if @body.key?(new_head)

    @snake.unshift(new_head)
    @body[new_head] = true

    if will_eat
      @score += 1
      @food_index += 1
    end

    @score
  end
end
