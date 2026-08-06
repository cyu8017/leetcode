object Solution {
  def getStrongest(arr: Array[Int], k: Int): Array[Int] = {
    val sorted = arr.sorted
    val median = sorted((sorted.length - 1) / 2)
    sorted.sortWith((a, b) => {
      val diff = math.abs(a - median) - math.abs(b - median)
      if (diff != 0) diff > 0 else a > b
    }).take(k)
  }
}
