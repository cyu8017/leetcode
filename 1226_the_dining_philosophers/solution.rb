# LeetCode 1226 - The Dining Philosophers
# https://leetcode.com/problems/the-dining-philosophers/

class DiningPhilosophers
  def initialize
    @forks = Array.new(5) { Mutex.new }
  end

  def wants_to_eat(philosopher, pick_left_fork, pick_right_fork, eat, put_left_fork, put_right_fork)
    left = philosopher
    right = (philosopher + 1) % 5
    first, second = philosopher.even? ? [left, right] : [right, left]
    @forks[first].synchronize do
      @forks[second].synchronize do
        pick_left_fork.call
        pick_right_fork.call
        eat.call
        put_left_fork.call
        put_right_fork.call
      end
    end
  end
end
