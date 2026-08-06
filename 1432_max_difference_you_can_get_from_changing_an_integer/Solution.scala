object Solution {
  def maxDiff(num: Int): Int = {
    val s = num.toString
    val high = s.find(_ != '9').map(c => s.replace(c, '9')).getOrElse(s)
    val low = if (s.head != '1') s.replace(s.head, '1')
    else s.drop(1).find(c => c != '0' && c != '1').map(c => s.replace(c, '0')).getOrElse(s)
    high.toInt - low.toInt
  }
}
