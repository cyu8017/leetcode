import java.time.LocalDate
import java.time.temporal.ChronoUnit

object Solution {
  def daysBetweenDates(date1: String, date2: String): Int =
    math.abs(ChronoUnit.DAYS.between(LocalDate.parse(date1), LocalDate.parse(date2))).toInt
}
