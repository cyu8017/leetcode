object Solution {
  def angleClock(hour: Int, minutes: Int): Double = {
    val difference = math.abs((hour % 12) * 30.0 + minutes * 0.5 - minutes * 6.0)
    math.min(difference, 360.0 - difference)
  }
}
