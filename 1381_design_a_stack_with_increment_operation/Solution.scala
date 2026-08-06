import scala.collection.mutable

class CustomStack(maxSize: Int) {
  private val values = mutable.ArrayBuffer.empty[Int]
  def push(x: Int): Unit = if (values.length < maxSize) values += x
  def pop(): Int = if (values.isEmpty) -1 else values.remove(values.length - 1)
  def increment(k: Int, `val`: Int): Unit = (0 until math.min(k, values.length)).foreach(i => values(i) += `val`)
}
