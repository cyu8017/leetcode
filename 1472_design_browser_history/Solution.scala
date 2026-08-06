class BrowserHistory(homepage: String) {
  private val history = scala.collection.mutable.ArrayBuffer(homepage)
  private var index = 0

  def visit(url: String): Unit = {
    history.trimEnd(history.length - index - 1)
    history += url
    index += 1
  }

  def back(steps: Int): String = {
    index = math.max(0, index - steps)
    history(index)
  }

  def forward(steps: Int): String = {
    index = math.min(history.length - 1, index + steps)
    history(index)
  }
}
