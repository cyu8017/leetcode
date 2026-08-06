object Solution {
  def destCity(paths: List[List[String]]): String = {
    val starts = paths.map(_(0)).toSet
    paths.find(p => !starts.contains(p(1))).get(1)
  }
}
