// LeetCode 1226 - The Dining Philosophers
// https://leetcode.com/problems/the-dining-philosophers/

class DiningPhilosophers() {
  private val forks = Array.fill(5)(new Object)

  def wantsToEat(
    philosopher: Int,
    pickLeftFork: Runnable,
    pickRightFork: Runnable,
    eat: Runnable,
    putLeftFork: Runnable,
    putRightFork: Runnable
  ): Unit = {
    val left = philosopher
    val right = (philosopher + 1) % 5
    val (first, second) = if (philosopher % 2 == 0) (left, right) else (right, left)
    forks(first).synchronized {
      forks(second).synchronized {
        pickLeftFork.run()
        pickRightFork.run()
        eat.run()
        putLeftFork.run()
        putRightFork.run()
      }
    }
  }
}
