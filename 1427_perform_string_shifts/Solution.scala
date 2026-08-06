object Solution {
  def stringShift(s: String, shift: Array[Array[Int]]): String = {
    var offset = shift.map(p => if (p(0) == 1) p(1) else -p(1)).sum % s.length
    if (offset < 0) offset += s.length
    s.takeRight(offset) + s.dropRight(offset)
  }
}
