object Solution {
  def isPathCrossing(path: String): Boolean = {
    var x = 0
    var y = 0
    val seen = scala.collection.mutable.HashSet((0, 0))
    for (direction <- path) {
      direction match {
        case 'N' => y += 1
        case 'S' => y -= 1
        case 'E' => x += 1
        case 'W' => x -= 1
      }
      if (!seen.add((x, y))) return true
    }
    false
  }
}
