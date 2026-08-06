object Solution {
  def processQueries(queries: Array[Int], m: Int): Array[Int] = { val a=scala.collection.mutable.ArrayBuffer((1 to m): _*); queries.map { x => val i=a.indexOf(x); a.remove(i); a.prepend(x); i } }
}
