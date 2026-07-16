object Solution {
  def read(file: String, queries: Array[Int]): Array[Int] = {
    var index = 0
    queries.map { query =>
      val count = math.min(query, file.length - index)
      index += count
      count
    }
  }
}