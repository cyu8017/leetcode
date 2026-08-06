object Solution {
  def displayTable(orders: List[List[String]]): List[List[String]] = {
    val foods = orders.map(_(2)).distinct.sorted
    val tables = orders.map(_(1).toInt).distinct.sorted
    val header = "Table" :: foods
    header :: tables.map { table =>
      table.toString :: foods.map(food => orders.count(order => order(1).toInt == table && order(2) == food).toString)
    }
  }
}
