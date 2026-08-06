// LeetCode 1117 - Building H2O
// https://leetcode.com/problems/building-h2o/

class H2O {
  private val hydrogen = new java.util.concurrent.Semaphore(2)
  private val oxygen = new java.util.concurrent.Semaphore(0)
  private val lock = new Object
  private var count = 0

  def hydrogen(releaseHydrogen: Runnable): Unit = {
    hydrogen.acquire()
    lock.synchronized {
      count += 1
      if (count == 2) oxygen.release()
    }
    releaseHydrogen.run()
  }

  def oxygen(releaseOxygen: Runnable): Unit = {
    oxygen.acquire()
    releaseOxygen.run()
    lock.synchronized {
      count = 0
      hydrogen.release()
      hydrogen.release()
    }
  }
}
